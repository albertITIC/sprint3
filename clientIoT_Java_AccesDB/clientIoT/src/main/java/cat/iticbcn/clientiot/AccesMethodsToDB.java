package cat.iticbcn.clientiot;

import java.sql.*;

import com.amazonaws.services.iot.client.AWSIotMessage;

public class AccesMethodsToDB {

    public void selectAlumnes (Connection con) {
        String sql = "SELECT * FROM alumne"; // Consulta SQL
        
        try (Statement stmt = con.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {
        
        while (rs.next()) {
            int id = rs.getInt("IdAlumne");
            String nombre = rs.getString("NomAlumne");
            System.out.println("ID: " + id + ", Nom: " + nombre);
        }
        
        } catch (SQLException e) {
            System.out.println("Error al ejecutar la consulta: " + e.getMessage());
        }


    }

    public void insertRegistry(Connection con, AWSIotMessage message) {

        //agafar el message.getStringPayload()
        //fer l'insert a la taula de registres

    }
    
}
