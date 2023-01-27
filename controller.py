import view
import processing
import log

def button_click():
    rezhim = view.inp_mod()
    if rezhim == 1:
        surname = view.inp_import()
        res_search = processing.search(surname)
        if isinstance(res_search, str):
            view.view_import_no(surname)
            log.log_cash('импорт', surname, 'не найдено')
        else:
            view.view_import(res_search)
            log.log_cash('импорт', surname, 'найдено')
    elif rezhim == 2:
        result = view.inp_export()
        processing.export(result)
        log.log_cash('экспорт', result[1], 'добавлено')