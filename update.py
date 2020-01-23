import os
from urllib.request import urlopen

for path, _, filenames in os.walk("."):
    for name in filenames:
        if name.endswith(".html"):
            name = os.path.join(path, name)
            if 'latest' in name:
                target = "https://python-gino.org/docs" + name.strip(".").replace(
                    "latest", "master"
                )
            elif name == './index.html':
                target = "https://python-gino.org/docs/"
            else:
                target = "https://python-gino.readthedocs.io" + name.strip(".")
            try:
                urlopen(target)
            except Exception:
                target = "https://python-gino.org/docs/"
            print(name, '>', target)
            with open(name, "w") as f:
                f.write(
                    f"""\
<!DOCTYPE HTML>
<html lang="en-US">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="refresh" content="0; url={target}">
        <script type="text/javascript">
            window.location.href = "{target}"
        </script>
        <title>Page Redirection</title>
    </head>
    <body>
        <!-- Note: don't tell people to `click` the link, just tell them that it is a link. -->
        If you are not redirected automatically, follow this <a href='{target}'>link to GINO docs</a>.
    </body>
</html>
"""
                )
