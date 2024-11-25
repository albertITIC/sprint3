package sprint3;

import com.fasterxml.jackson.databind.ObjectMapper;

public class Assistencia {
    private int idUsuari;
    private String estat;
    private String hEntrada;
    private String hSortida;
    private String dia;

    // Getters i setters
    public int getIdUsuari() { return idUsuari; }
    public void setIdUsuari(int idUsuari) { this.idUsuari = idUsuari; }
    public String getEstat() { return estat; }
    public void setEstat(String estat) { this.estat = estat; }
    public String getHEntrada() { return hEntrada; }
    public void setHEntrada(String hEntrada) { this.hEntrada = hEntrada; }
    public String getHSortida() { return hSortida; }
    public void setHSortida(String hSortida) { this.hSortida = hSortida; }
    public String getDia() { return dia; }
    public void setDia(String dia) { this.dia = dia; }

    public static Assistencia fromJson(String json) throws Exception {
        ObjectMapper mapper = new ObjectMapper();
        return mapper.readValue(json, Assistencia.class);
    }
}
