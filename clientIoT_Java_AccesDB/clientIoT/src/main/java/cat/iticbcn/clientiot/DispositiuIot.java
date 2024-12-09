/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package cat.iticbcn.clientiot;

/**
 *
 * @author DAW I DAM
 */
import com.amazonaws.services.iot.client.AWSIotException;
import com.amazonaws.services.iot.client.AWSIotMqttClient;
import com.amazonaws.services.iot.client.AWSIotQos;
import com.amazonaws.services.iot.client.sample.sampleUtil.SampleUtil;
import com.amazonaws.services.iot.client.sample.sampleUtil.SampleUtil.KeyStorePasswordPair;

public class DispositiuIot{

    //private static final String FICH_CLAU_PUBLICA = "./client1certs/";
    private static final String FICH_CLAU_PRIVADA = "/home/isard/Escriptori/Projecte/sprint3/clientIoT_Java_AccesDB/clientIoT/client1certs/client1-private.pem.key";
    private static final String FICH_CERT_DISP_IOT = "/home/isard/Escriptori/Projecte/sprint3/clientIoT_Java_AccesDB/clientIoT/client1certs/client1-certificate.pem.crt";
    private static final String ENDPOINT = "a3hvwfbfayc3f6-ats.iot.us-east-1.amazonaws.com";
    public static final String TOPIC = "esp32/esp32-to-aws";
    public static final String CLIENT_ID = "ESP32-thing";
    public static final AWSIotQos TOPIC_QOS = AWSIotQos.QOS0;

    private static AWSIotMqttClient awsIotClient;

    public static void setClient(AWSIotMqttClient cli) {
        awsIotClient = cli;
    }

    public static void initClient() {
        String cliEP = ENDPOINT;
        String cliId = CLIENT_ID;

        String certFile = FICH_CERT_DISP_IOT;
        String pKFile = FICH_CLAU_PRIVADA;

        if (awsIotClient == null && certFile != null && pKFile != null) {
            String algorithm = null;
            
            KeyStorePasswordPair pair = SampleUtil.getKeyStorePasswordPair(certFile, pKFile, algorithm);

            awsIotClient = new AWSIotMqttClient(cliEP, cliId, pair.keyStore, pair.keyPassword);
        }

        if (awsIotClient == null) {
            throw new IllegalArgumentException("Error als construir client amb el certificat o les credencials.");
        }
    }

    public void conecta() throws AWSIotException{
        initClient();
        awsIotClient.connect();
    }

    public void subscriu() throws AWSIotException{
        TopicIoT topic= new TopicIoT(TOPIC, TOPIC_QOS);
        awsIotClient.subscribe(topic, true);
    }
}