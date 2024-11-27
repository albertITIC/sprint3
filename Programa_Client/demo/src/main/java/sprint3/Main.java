package sprint3;

import software.amazon.awssdk.services.sqs.model.Message;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        AWSClient awsClient = new AWSClient();
        DatabaseClient dbClient = new DatabaseClient();

        try {
            List<Message> messages = awsClient.receiveMessages();

            for (Message message : messages) {
                try {
                    // Processa el JSON rebut
                    Assistencia assistencia = Assistencia.fromJson(message.body());

                    // Insereix a la base de dades
                    dbClient.insertAssistencia(
                            assistencia.getIdUsuari(),
                            assistencia.getEstat(),
                            assistencia.getHEntrada(),
                            assistencia.getHSortida(),
                            assistencia.getDia()
                    );

                    // Elimina el missatge processat
                    awsClient.deleteMessage(message.receiptHandle());
                    System.out.println("Assistència processada correctament: " + assistencia);
                } catch (Exception e) {
                    System.err.println("Error processant missatge: " + e.getMessage());
                }
            }
        } finally {
            awsClient.close();
        }
    }
}
