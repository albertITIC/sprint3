package sprint3;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class DatabaseClient {
    private static final String DB_URL = "jdbc:mariadb://localhost:3306/AppAssistencies";
    private static final String DB_USER = "root";
    private static final String DB_PASSWORD = "your_password";

    public Connection connect() throws SQLException {
        return DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD);
    }

    public void insertAssistencia(int idUsuari, String estat, String hEntrada, String hSortida, String dia) {
        String query = "INSERT INTO Assistencia (idUsuari, estat, hEntrada, hSortida, dia) VALUES (?, ?, ?, ?, ?)";
        try (Connection conn = connect(); PreparedStatement pstmt = conn.prepareStatement(query)) {
            pstmt.setInt(1, idUsuari);
            pstmt.setString(2, estat);
            pstmt.setString(3, hEntrada);
            pstmt.setString(4, hSortida);
            pstmt.setString(5, dia);
            pstmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
