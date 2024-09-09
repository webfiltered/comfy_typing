# Mixins that could be used for type-hinting and docstrings.

# class IsChangedMixin:
#     """
#     Mixin providing IS_CHANGED type hinting for nodes that implement their own routine to check for changes.

#     https://docs.comfy.org/essentials/custom_node_server_overview#is-changed
#     """

#     @classmethod
#     def IS_CHANGED(self) -> Any:
#         """
#         Run before executing the node.  The value returned by this function is compared to the last value it sent.
#         If they match, execution is skipped and Comfy uses cached results of the last execution.
#         """
#         pass


# class ValidateInputsMixin:
#     """
#     Mixin providing VALIDATE_INPUTS for nodes that handle their own validation checks.

#     https://docs.comfy.org/essentials/custom_node_server_overview#validate-inputs
#     """

#     @classmethod
#     def VALIDATE_INPUTS(self) -> str | Literal[True]:
#         """
#         Validates constant values input to the node.  Returns True for success or a string error message.
#         ComfyUI documentation has specific details.

#         https://docs.comfy.org/essentials/custom_node_server_overview#validate-inputs
#         """
#         pass
