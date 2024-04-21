from Config.Util import *
from Config.Config import *
Title("Tool Info")
print(f"{color.RED}{WAIT} Information Recovery..{reset}")
print(f"""{color.RED}
{color.RED}Name Tool     :  {color.WHITE}{name_tool}
{color.RED}Version       :  {color.WHITE}{version_tool}
{color.RED}Coding        :  {color.WHITE}{coding_tool}
{color.RED}Language      :  {color.WHITE}{language_tool}
{color.RED}Creator       :  {color.WHITE}{creator}
{color.RED}Platform      :  {color.WHITE}{platform}
{color.RED}Discord [02]  :  {color.WHITE}{discord_server}
{color.RED}Site    [02]  :  {color.WHITE}{website}
{color.RED}GitHub  [02]  :  {color.WHITE}{github_tool}
""" + color.RESET)

Continue()
Reset()