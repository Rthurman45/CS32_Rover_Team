import subprocess
import time
import pytest


@pytest.fixture
def publisher_process():
    process = subprocess.Popen(
        ['ros2', 'run', 'ros2_topic_skeleton', 'topic_publisher'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    yield process

    process.terminate()

    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait()


def test_topics_exist(publisher_process):
    expected_topics = {
        '/temp_topic_1',
        '/temp_topic_2'
    }

    discovered_topics = set()

    timeout = time.time() + 30

    while time.time() < timeout:

        if publisher_process.poll() is not None:
            pytest.fail('Publisher process exited unexpectedly')

        result = subprocess.run(
            ['ros2', 'topic', 'list'],
            capture_output=True,
            text=True
        )

        discovered_topics = set(
            result.stdout.strip().splitlines()
        )

        if expected_topics.issubset(discovered_topics):
            break

        time.sleep(1)

    missing_topics = expected_topics - discovered_topics

    assert not missing_topics, (
        f'Missing ROS 2 topics: {missing_topics}'
    )