@pushd %~dp0
sphinx-build -b html docs build/sphinx/html -E -a -W

@IF "%1" NEQ "SILENT" (
    build\sphinx\html\index.html
)

@popd

@IF "%1" NEQ "SILENT" (
    PAUSE
)
