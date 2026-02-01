"""Unit tests for agent-cli singleton module."""

import pytest
from agent_cli.singleton import Singleton


class TestSingleton:
    """Tests for Singleton metaclass."""

    @pytest.fixture(autouse=True)
    def setup(self, clear_singleton: None) -> None:
        """Clear singleton instances before each test."""

    def test_same_instance_returned(self) -> None:
        """Multiple instantiations should return the same instance."""

        class MySingleton(metaclass=Singleton):
            def __init__(self, value: int = 0):
                self.value = value

        first = MySingleton(1)
        second = MySingleton(2)

        assert first is second
        assert first.value == 1  # First value preserved

    def test_different_classes_independent(self) -> None:
        """Different singleton classes should have independent instances."""

        class SingletonA(metaclass=Singleton):
            pass

        class SingletonB(metaclass=Singleton):
            pass

        a = SingletonA()
        b = SingletonB()

        assert a is not b
        assert isinstance(a, SingletonA)
        assert isinstance(b, SingletonB)

    def test_clear_instances(self) -> None:
        """Clearing _instances should allow new instance creation."""

        class MySingleton(metaclass=Singleton):
            def __init__(self, value: int = 0):
                self.value = value

        first = MySingleton(1)
        Singleton._instances.clear()  # pyright: ignore[reportPrivateUsage]
        second = MySingleton(2)

        assert first is not second
        assert second.value == 2
