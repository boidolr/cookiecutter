from {{cookiecutter.module_name}} import hook


def test_hook(tmp_path):
    path = tmp_path / "file"
    path.write_text("# file content")

    assert hook.main((str(path),)) == 0
