#  Copyright Software Improvement Group
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from functools import lru_cache

from report_generator.generator.context import sigrid_api
from report_generator.generator.context.portfolio_filters import get_filter_values

from .base import text_placeholder


@lru_cache(maxsize=1)
def _get_filtered_systems():
    """Get systems filtered by team, cached."""
    portfolio_data = sigrid_api.get_portfolio_maintainability()
    systems = portfolio_data.get("systems", []) if isinstance(portfolio_data, dict) else []
    return systems


@text_placeholder()
def team_name():
    """The name of the team from the filter parameter."""
    teams = get_filter_values("team")
    return teams[0] if teams else "Team"


@text_placeholder()
def system_name_1():
    """First system name in the team."""
    systems = _get_filtered_systems()
    return systems[0].get("systemName", "") if systems else ""


@text_placeholder()
def system_name_2():
    """Second system name in the team."""
    systems = _get_filtered_systems()
    return systems[1].get("systemName", "") if len(systems) > 1 else ""


@text_placeholder()
def system_name_3():
    """Third system name in the team."""
    systems = _get_filtered_systems()
    return systems[2].get("systemName", "") if len(systems) > 2 else ""


@text_placeholder()
def system_name_4():
    """Fourth system name in the team."""
    systems = _get_filtered_systems()
    return systems[3].get("systemName", "") if len(systems) > 3 else ""


@text_placeholder()
def system_name_5():
    """Fifth system name in the team."""
    systems = _get_filtered_systems()
    return systems[4].get("systemName", "") if len(systems) > 4 else ""


@text_placeholder()
def repos_1():
    """Repos for first system (x van y format)."""
    systems = _get_filtered_systems()
    if not systems:
        return ""
    system = systems[0]
    repos_analyzed = system.get("reposAnalyzed", 0)
    repos_total = system.get("reposTotal", 0)
    return f"{repos_analyzed} van {repos_total}" if repos_total > 0 else ""


@text_placeholder()
def repos_2():
    """Repos for second system (x van y format)."""
    systems = _get_filtered_systems()
    if len(systems) < 2:
        return ""
    system = systems[1]
    repos_analyzed = system.get("reposAnalyzed", 0)
    repos_total = system.get("reposTotal", 0)
    return f"{repos_analyzed} van {repos_total}" if repos_total > 0 else ""


@text_placeholder()
def repos_3():
    """Repos for third system (x van y format)."""
    systems = _get_filtered_systems()
    if len(systems) < 3:
        return ""
    system = systems[2]
    repos_analyzed = system.get("reposAnalyzed", 0)
    repos_total = system.get("reposTotal", 0)
    return f"{repos_analyzed} van {repos_total}" if repos_total > 0 else ""


@text_placeholder()
def repos_4():
    """Repos for fourth system (x van y format)."""
    systems = _get_filtered_systems()
    if len(systems) < 4:
        return ""
    system = systems[3]
    repos_analyzed = system.get("reposAnalyzed", 0)
    repos_total = system.get("reposTotal", 0)
    return f"{repos_analyzed} van {repos_total}" if repos_total > 0 else ""


@text_placeholder()
def repos_5():
    """Repos for fifth system (x van y format)."""
    systems = _get_filtered_systems()
    if len(systems) < 5:
        return ""
    system = systems[4]
    repos_analyzed = system.get("reposAnalyzed", 0)
    repos_total = system.get("reposTotal", 0)
    return f"{repos_analyzed} van {repos_total}" if repos_total > 0 else ""


placeholders = {
    team_name,
    system_name_1,
    system_name_2,
    system_name_3,
    system_name_4,
    system_name_5,
    repos_1,
    repos_2,
    repos_3,
    repos_4,
    repos_5,
}
