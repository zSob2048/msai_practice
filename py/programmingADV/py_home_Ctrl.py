

from py_console_Screen import console_screen
from py_objectDAO import productDAO, sellerDAO


if __name__ == "__main__":
    sellerDAO = sellerDAO()
    productDAO = productDAO()

    while True:
        menu = console_screen.page_main_print()

        if menu == "10":
            break

        elif menu == "1":
            seller = console_screen.page_1_print()
            result = sellerDAO.reg(seller)
            console_screen.result_print(result)

        elif menu == "2":
            product = console_screen.page_2_print()
            result = productDAO.reg()
            console_screen.result_print(result)
        
        elif menu == "3":
            page_all = sellerDAO.count_page()
            page = console_screen.input_pagenum(page_all)
            page_list = sellerDAO.all_list_page(page)
            console_screen.page_3_print(page_list)
        
        elif menu == "4":
            page_all = productDAO.count_page()
            page = console_screen.input_pagenum(page_all)
            page_list = productDAO.all_list_page(page)
            console_screen.page_3_print(page_list)

