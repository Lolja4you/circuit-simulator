def is_result(ciruit):
    try:
        if ciruit.result:...
        if ciruit.is_changed:
            from my_mind.test_branches import test
            test.calc(ciruit)        
            ciruit.is_changed = False

    except AttributeError:
        from my_mind.test_branches import test
        try:
            test.calc(ciruit)
            return True
        except (AttributeError, TypeError):
            from tkinter import messagebox
            messagebox.showerror("Ошибка", "Схема не собрана")
            return False
