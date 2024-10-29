def test_node_exists():
    try:
        from experta.matchers.rete.abstract import Node  # noqa: F401
        from experta.matchers.rete.abstract import OneInputNode  # noqa: F401
        from experta.matchers.rete.abstract import TwoInputNode  # noqa: F401
    except ImportError as exc:
        assert False, exc


def test_node_interface():
    from experta.matchers.rete.abstract import Node

    assert {"_reset", "add_child"} <= Node.__abstractmethods__


def test_oneinputnode_interface():
    from experta.matchers.rete.abstract import OneInputNode

    assert {"_activate"} <= OneInputNode.__abstractmethods__


def test_twoinputnode_interface():
    from experta.matchers.rete.abstract import TwoInputNode

    assert {
        "_activate_left",
        "_activate_right",
    } <= TwoInputNode.__abstractmethods__
