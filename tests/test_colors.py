def test_colors_get_printed(pytester):
    pytester.copy_example("examples/test_example.py")
    pytester.makepyfile(__init__ = "")
    result = pytester.runpytest("-s")
    result.assert_outcomes(passed=1)
    bold, reset  = '\x1b[1m', '\x1b[0m'
    result.stdout.fnmatch_lines(
        [
            f"*{bold}\x1b[31mtest_colors: this should be red{reset}",
            f"*{bold}\x1b[32mtest_colors: this should be green{reset}",
            f"*{bold}\x1b[33mtest_colors: this should be yellow{reset}",
            f"*{bold}\x1b[34mtest_colors: this should be blue{reset}",
            f"*{bold}\x1b[35mtest_colors: this should be magenta{reset}",
            f"*{bold}\x1b[36mtest_colors: this should be cyan{reset}",
        ],
    )

def test_no_crayons(pytester):
    pytester.copy_example("examples/test_example.py")
    pytester.makepyfile(__init__ = "")
    result = pytester.runpytest("-s", "--no-crayons")
    result.assert_outcomes(passed=1)
    bold, reset  = '\x1b[1m', '\x1b[0m'
    result.stdout.fnmatch_lines(
        [
            "*this should be red",
            "*this should be green",
            "*this should be yellow",
            "*this should be blue",
            "*this should be magenta",
            "*this should be cyan",
        ],
    )
    result.stdout.no_fnmatch_line("*\x1b[*")  # no color codes
    result.stdout.no_fnmatch_line("*test_colors*")  # no test name prefix
    result.stdout.no_fnmatch_line(f"*{bold}*")  # no bold
    result.stdout.no_fnmatch_line(f"*{reset}*")  # no reset
