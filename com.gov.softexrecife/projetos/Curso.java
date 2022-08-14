package com.gov.softexrecife.projetos;

import java.util.List;

public interface Curso {
    int getId();
    void setId();
    String getNome();
    void setNome();
    List getResposaveis();
    void setResposaveis();
    int getDuração();
}
