class AccountNotFoundError(Exception):
    """Lançado quando a conta não é encontrada no banco de dados."""
    pass


class BusinessError(Exception):
    """Lançado quando há erro de regra de negócio (ex: saldo insuficiente)."""
    pass
