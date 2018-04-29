#!/usr/bin/python3
# da desc na tabela para pegar os valores e automatizat oM.query
import gi
import Imports

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

oM = Imports.Mysqli()
cursor = oM.Con.cursor()


class Faculdade:
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("Faculdade.glade")

        self.window1 = builder.get_object("window1")
        self.entryNome = builder.get_object("entryNome")
        self.entrySobrenome = builder.get_object("entrySobrenome")
        self.rbtSexo = builder.get_object("rbtSexoM")
        self.entryEmail = builder.get_object("entryEmail")
        self.entryTelefone = builder.get_object("entryTelefone")
        self.entryCurso = builder.get_object("entryCurso")

        self.btnCadastrar = builder.get_object("btnCadastrar")
        self.btnLimpar = builder.get_object("btnLimpar")

        self.window1.show()

        builder.connect_signals({"gtk_main_quit": Gtk.main_quit,
                                 "on_btnGravar_clicked": self.cadastrar,
                                 "on_btnLimpar_clicked": self.limpar})

    def cadastrar(self, widget):
        sexo = ""
        option = self.get_active_radio()
        if option == "Masculino":
            sexo = "M"

        elif option == "Feminino":
            sexo = "F"

        oM.query("INSERT INTO Aluno (Nome, Sobrenome, Sexo, Email, Telefone, Curso) value"
                 "('{}', '{}', '{}', '{}', '{}', '{}');".format(
                    self.entryNome.get_text(),
                    self.entrySobrenome.get_text(),
                    sexo,
                    self.entryEmail.get_text(),
                    self.entryTelefone.get_text(),
                    self.entryCurso.get_text()))

    def limpar(self, widget):
        self.entryNome.set_text("")
        self.entrySobrenome.set_text("")
        self.entryEmail.set_text("")
        self.entryTelefone.set_text("")
        self.entryCurso.set_text("")

    def get_active_radio(self):
        radiobtn = self.rbtSexo.get_group()

        for radio in radiobtn:
            if radio.get_active():
                return radio.get_label()


if __name__ == '__main__':
    oF = Faculdade()
    Gtk.main()
