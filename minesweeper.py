from tkinter import*
from random import*
from tkinter import ttk

class Sucelje1(Frame):
    def __init__(self, root):
        self.root=root
        self.root.title('Upit')
        super().__init__(self.root)
        self.grid(rows=3, columns=2)
        self.KreirajSucelje()
        return

    def KreirajSucelje(self):
        self.L=Label(self, text='Broj stupaca i redaka')
        self.L.grid(row=1, column=1)
        self.E=Entry(self)
        self.E.grid(row=1, column=2)
        self.L1=Label(self, text='Broj bombica: ')
        self.L1.grid(row=2, column=1)
        self.E1=Entry(self)
        self.E1.grid(row=2, column=2)
        self.B=Button(self, text='OKAY', command=self.Click)
        self.B.grid(row=3, column=1, columnspan=2)
        return

    def Click(self):
        try:
            self.a=int(self.E.get())
            self.b=int(self.E1.get())
            self.novi=Program(Tk(), self.a, self.b)
            self.root.destroy()
            self.novi.mainloop()
        except ValueError:
            print('Molimo unesite tražene brojke')
        return


class Gumb(Button):
    def __init__(self, vrijednost, b, gumb, dis, flag):
        self.vrijednost=vrijednost
        self.brojbombicaokolo=b
        self.gumbic=gumb
        self.dis=dis
        self.flag=flag
        return



class Program(Frame):
    def __init__(self, prozor, a, b):
        self.prozor=prozor
        self.brojka=a
        self.broj_bomba=b
        self.prozor.resizable(False, False)
        self.prozor.title('Minesweeper')
        super().__init__(self.prozor)
        self.grid(rows=1, columns=2)
        self.KreirajSucelje()
        return

    def KreirajSucelje(self):
        x=0
        self.btn=[[0 for i in range(self.brojka)] for i in range(self.brojka)]
        for i in range(self.brojka):
            for j in range(self.brojka):
                s=0
                self.btn[i][j]=Gumb(0, 0, Button(self, text ='', command= lambda i=i, j=j: self.Klik(i,j), width=2, bg='grey'), 0, 0)
                self.btn[i][j].gumbic.bind('<Button-3>', lambda s=s, i=i, j=j: self.DesniKlik(i, j))
                self.btn[i][j].gumbic.grid(row=i+1, column=j+1)

        h=0   
        while h<self.broj_bomba:
            x=randint(0, self.brojka-1)
            y=randint(0, self.brojka-1)
            if self.btn[x][y].vrijednost==0:
                self.btn[x][y].vrijednost+=1
                self.btn[x][y].gumbic.config(text='')
                h+=1

    
        
        for a in range(self.brojka):
            for b in range(self.brojka):
                if self.brojka-1>a>0 and self.brojka-1>b>0:
                    self.btn[a][b].brojbombicaokolo=self.btn[a-1][b-1].vrijednost+self.btn[a-1][b].vrijednost+self.btn[a][b-1].vrijednost+self.btn[a][b+1].vrijednost+self.btn[a+1][b].vrijednost+self.btn[a+1][b+1].vrijednost+self.btn[a-1][b+1].vrijednost+self.btn[a+1][b-1].vrijednost
                ##PeTLJA 1
                elif a==0 and self.brojka-1>b>0:
                    self.btn[a][b].brojbombicaokolo=self.btn[a][b-1].vrijednost+self.btn[a][b+1].vrijednost+self.btn[a+1][b].vrijednost+self.btn[a+1][b+1].vrijednost+self.btn[a+1][b-1].vrijednost
                ##PeTLJA 2
                elif self.brojka-1>a>0 and b==self.brojka-1:
                    self.btn[a][b].brojbombicaokolo=self.btn[a-1][b-1].vrijednost+self.btn[a-1][b].vrijednost+self.btn[a][b-1].vrijednost+self.btn[a+1][b].vrijednost+self.btn[a+1][b-1].vrijednost
                ##PeTLJA 3
                elif a==self.brojka-1 and self.brojka-1>b>0:
                    self.btn[a][b].brojbombicaokolo=self.btn[a-1][b-1].vrijednost+self.btn[a-1][b].vrijednost+self.btn[a][b-1].vrijednost+self.btn[a][b+1].vrijednost+self.btn[a-1][b+1].vrijednost
                ##PeTLJA 4
                elif self.brojka-1>a>0 and b==0:
                    self.btn[a][b].brojbombicaokolo=self.btn[a-1][b].vrijednost+self.btn[a][b+1].vrijednost+self.btn[a+1][b].vrijednost+self.btn[a+1][b+1].vrijednost+self.btn[a-1][b+1].vrijednost
                ##PeTLJA 5
                elif a==0 and b==0:
                    self.btn[a][b].brojbombicaokolo=self.btn[a][b+1].vrijednost+self.btn[a+1][b].vrijednost+self.btn[a+1][b+1].vrijednost
                ##PeTLJA 6
                elif a==0 and b==self.brojka-1:
                    self.btn[a][b].brojbombicaokolo=self.btn[a+1][b].vrijednost+self.btn[a+1][b-1].vrijednost+self.btn[a][b-1].vrijednost
                ##PeTLJA 7
                elif a==self.brojka-1 and b==self.brojka-1:
                    self.btn[a][b].brojbombicaokolo=self.btn[a-1][b].vrijednost+self.btn[a][b-1].vrijednost+self.btn[a-1][b-1].vrijednost
                ##PeTLJA 8
                elif a==self.brojka-1 and b==0:
                    self.btn[a][b].brojbombicaokolo=self.btn[a-1][b].vrijednost+self.btn[a][b+1].vrijednost+self.btn[a-1][b+1].vrijednost   
        return
             

    def Klik(self, a, b):
        if self.btn[a][b].dis==0:
            self.btn[a][b].dis=1
            boje=['blue', 'green', 'red', 'purple', 'maroon', 'turquoise', 'black', 'gray']
            if self.btn[a][b].vrijednost==0:
                self.btn[a][b].gumbic.config(state='disabled')
                if self.btn[a][b].brojbombicaokolo!=0:
                    self.btn[a][b].gumbic.config(text=self.btn[a][b].brojbombicaokolo, disabledforeground=boje[self.btn[a][b].brojbombicaokolo-1], bg='white')
                else:
                    self.btn[a][b].gumbic.config(text='', bg='white')
            else:
                for i in range(self.brojka):
                    for j in range(self.brojka):
                        self.btn[i][j].dis=1
                        self.btn[i][j].gumbic.config(state='disabled')
                        if self.btn[i][j].vrijednost==1:
                            self.btn[i][j].gumbic.config(text='X', fg='black', background='pink')
                self.kraj2=Kraj2(Tk(), self.prozor)
                self.kraj2.mainloop()


            if self.btn[a][b].brojbombicaokolo==0:
                 if self.btn[a][b].vrijednost==0:
                     if self.brojka-1>a>0 and self.brojka-1>b>0:
                        self.btn[a-1][b-1].gumbic.config(command=self.Klik(a-1, b-1))
                        self.btn[a][b-1].gumbic.config(command=self.Klik(a, b-1))
                        self.btn[a+1][b-1].gumbic.config(command=self.Klik(a+1, b-1))
                        self.btn[a][b+1].gumbic.config(command=self.Klik(a, b+1))
                        self.btn[a-1][b].gumbic.config(command=self.Klik(a-1, b))
                        self.btn[a+1][b].gumbic.config(command=self.Klik(a+1, b))
                        self.btn[a+1][b+1].gumbic.config(command=self.Klik(a+1, b+1))
                        self.btn[a-1][b+1].gumbic.config(command=self.Klik(a-1, b+1))
                        
                     #PETLJA 1
                     elif a==0 and b==0:
                         self.btn[a][b+1].gumbic.config(command=self.Klik(a, b+1))
                         self.btn[a+1][b].gumbic.config(command=self.Klik(a+1, b))
                         self.btn[a+1][b+1].gumbic.config(command=self.Klik(a+1, b+1))
                        

                     #PETLJA 2
                     elif a==0 and self.brojka-1>b>0:
                         self.btn[a][b-1].gumbic.config(command=self.Klik(a, b-1))
                         self.btn[a+1][b-1].gumbic.config(command=self.Klik(a+1, b-1))
                         self.btn[a][b+1].gumbic.config(command=self.Klik(a, b+1))
                         self.btn[a+1][b].gumbic.config(command=self.Klik(a+1, b))
                         self.btn[a+1][b+1].gumbic.config(command=self.Klik(a+1, b+1))
                        
                     #PETLJA 3
                     elif a==0 and b==self.brojka-1:
                         self.btn[a][b-1].gumbic.config(command=self.Klik(a, b-1))
                         self.btn[a+1][b-1].gumbic.config(command=self.Klik(a+1, b-1))
                         self.btn[a+1][b].gumbic.config(command=self.Klik(a+1, b))
                        
                     #PETLJA 4
                     elif self.brojka-1>a>0 and b==0:
                         self.btn[a][b+1].gumbic.config(command=self.Klik(a, b+1))
                         self.btn[a-1][b].gumbic.config(command=self.Klik(a-1, b))
                         self.btn[a+1][b].gumbic.config(command=self.Klik(a+1, b))
                         self.btn[a+1][b+1].gumbic.config(command=self.Klik(a+1, b+1))
                         self.btn[a-1][b+1].gumbic.config(command=self.Klik(a-1, b+1))
                        
                     #PETLJA 5
                     elif self.brojka-1>a>0 and b==self.brojka-1:
                         self.btn[a-1][b-1].gumbic.config(command=self.Klik(a-1, b-1))
                         self.btn[a][b-1].gumbic.config(command=self.Klik(a, b-1))
                         self.btn[a+1][b-1].gumbic.config(command=self.Klik(a+1, b-1))
                         self.btn[a-1][b].gumbic.config(command=self.Klik(a-1, b))
                         self.btn[a+1][b].gumbic.config(command=self.Klik(a+1, b))
                        
                     #PETLJA 6
                     elif a==self.brojka-1 and b==0:
                         self.btn[a][b+1].gumbic.config(command=self.Klik(a, b+1))
                         self.btn[a-1][b+1].gumbic.config(command=self.Klik(a-1, b+1))
                         self.btn[a-1][b].gumbic.config(command=self.Klik(a-1, b))
                        
                     #PETLJA 7
                     elif a==self.brojka-1 and self.brojka-1>b>0:
                         self.btn[a-1][b-1].gumbic.config(command=self.Klik(a-1, b-1))
                         self.btn[a][b-1].gumbic.config(command=self.Klik(a, b-1))
                         self.btn[a][b+1].gumbic.config(command=self.Klik(a, b+1))
                         self.btn[a-1][b].gumbic.config(command=self.Klik(a-1, b))
                         self.btn[a-1][b+1].gumbic.config(command=self.Klik(a-1, b+1))
                        
                     #PETLJA 8
                     elif a==self.brojka-1 and b==self.brojka-1:
                         self.btn[a-1][b-1].gumbic.config(command=self.Klik(a-1, b-1))
                         self.btn[a][b-1].gumbic.config(command=self.Klik(a, b-1))
                         self.btn[a-1][b].gumbic.config(command=self.Klik(a-1, b))
        return

    def DesniKlik(self, a, b):
        if self.btn[a][b].dis==0:
            self.btn[a][b].dis=1
            self.btn[a][b].gumbic.config(text='F', fg='red')
            self.btn[a][b].flag=1
            s=0
            for i in range(self.brojka):
                for j in range(self.brojka):
                    if self.btn[i][j].flag==1 and self.btn[i][j].vrijednost==1:
                        s+=1
            if s==self.broj_bomba:
                self.Kraj=Kraj1(Tk(), self.prozor)
                self.Kraj.mainloop()
                
        else:
            if self.btn[a][b].flag==1:
                self.btn[a][b].dis=0
                self.btn[a][b].gumbic.config(text='', fg='black')
            
        return


class Kraj1(Frame):
    def __init__(self, root, prozor):
        self.root=root
        self.prozor=prozor
        self.root.title('Pobijedili ste!')
        super().__init__(self.root)
        self.grid(rows=2, columns=1)
        self.KreirajSucelje()
        return

    def KreirajSucelje(self):
        self.L=Label(self, text='Cestitamo, pobijedili ste!\nIgrati ponovno?')
        self.L.grid(row=1, column=1)
        self.B=Button(self, text='Da', command=self.Klik, padx=10, pady=10)
        self.B.grid(rows=2, column=1)
        return

    def Klik(self):
        self.prozor.destroy()
        self.upit=Sucelje1(Tk())
        self.root.destroy()
        self.upit.mainloop()
        return
        

class Kraj2(Frame):
    def __init__(self, root, prozor):
        self.root=root
        self.prozor=prozor
        self.root.title('Pobijedili ste!')
        super().__init__(self.root)
        self.grid(rows=2, columns=1)
        self.KreirajSucelje()
        return

    def KreirajSucelje(self):
        self.L=Label(self, text='Izgubili ste!\nPokusati ponovno?')
        self.L.grid(row=1, column=1)
        self.B=Button(self, text='Da', command=self.Klik, padx=10, pady=10)
        self.B.grid(rows=2, column=1)
        return

    def Klik(self):
        self.prozor.destroy()
        self.upit=Sucelje1(Tk())
        self.root.destroy()
        self.upit.mainloop()
        return

def main():
    p=Sucelje1(Tk())
    mainloop()
    return

main()
