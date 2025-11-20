import Question

class MultipleChoiceQuestion(Question):
    """
        Responsável por guardar os dados das questões de multipla escolha.
        - Deve implementar o método check_answer()!!!!!!
    """
    def __init__(self, options: list, correct_option_index: int):
        super().__init__()
        raise NotImplementedError("Unimplemented feature.")