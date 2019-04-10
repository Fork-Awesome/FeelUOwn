class Request:
    """fuo 协议请求对象"""

    def __init__(self, cmd, cmd_args=None,
                 cmd_options=None, options=None,
                 has_heredoc=False, heredoc_word=None):
        self.cmd = cmd
        self.cmd_args = cmd_args or []
        self.cmd_options = cmd_options or {}

        self.options = options or {}

        self.has_heredoc = has_heredoc
        self.heredoc_word = heredoc_word
