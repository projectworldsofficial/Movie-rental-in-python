from domain.Borrow import Borrow
from domain.Rental import Rental 
from repository.BorrowRepository import BorrowRepository
from repository.DvdRepository import DvdRepository
from domain.Dvd import Dvd
from controller.Controller import Controller
from ui.UI import UI

def main():
    BorrowRepo = BorrowRepository("borrow.txt")
    DvdRepo = DvdRepository("dvd.txt")
    
    ctrl = Controller(BorrowRepo,DvdRepo) 
    ui = UI(ctrl)
    ui.run()
    
main()