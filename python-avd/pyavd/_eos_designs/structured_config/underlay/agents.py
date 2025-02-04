# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from . import AvdStructuredConfigUnderlayProtocol


class AgentsMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def agents(self: AvdStructuredConfigUnderlayProtocol) -> None:
        """Set the structured config for agents."""
        if not self.shared_utils.is_wan_router:
            return

        env_var = EosCliConfigGen.AgentsItem.EnvironmentVariables()
        env_var.append(EosCliConfigGen.AgentsItem.EnvironmentVariablesItem(name="KERNELFIB_PROGRAM_ALL_ECMP", value="1"))
        self.structured_config.agents.append(EosCliConfigGen.AgentsItem(name="KernelFib", environment_variables=env_var))
