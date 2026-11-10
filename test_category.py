"""Unit tests for Category.get_by_section (no CLI interaction)."""

import yaml

from model.category import Category


def _write_structure(tmp_path, data):
    data_dir = tmp_path / "data"
    data_dir.mkdir(exist_ok=True)
    with open(data_dir / "structure.yaml", "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f)


def test_get_by_section_returns_categories(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    _write_structure(tmp_path, {"Tools": {"order": 1, "categories": [{"name": "Editors"}]}})

    assert Category().get_by_section("Tools") == [{"name": "Editors"}]


def test_get_by_section_with_null_section_value(tmp_path, monkeypatch):
    """A section with no body must not crash category lookup."""
    monkeypatch.chdir(tmp_path)
    (tmp_path / "data").mkdir(exist_ok=True)
    (tmp_path / "data" / "structure.yaml").write_text("EmptySection:\n", encoding="utf-8")

    assert Category().get_by_section("EmptySection") == []


def test_get_by_section_missing_section(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    _write_structure(tmp_path, {"Tools": {"order": 1, "categories": []}})

    assert Category().get_by_section("Nope") == []
