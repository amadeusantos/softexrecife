package com.gov.softexrecife.funcionarios;

import java.util.List;

public interface Desenvolvedor {
    int getId();
    void setId();
    String getNome();
    void setNome();
    String getCargo();
    void setCargo();
    int getIdade();
    List getProjetos();
    void setProjetos();
}
