package test.wrx.myhttptest;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;

public class SocketClient {

    public static void main(String[] args) {

        String uri = "/MyWebTest/ReturnServlet";

        Socket socket = null;
        try {
            socket = new Socket("10.0.161.30",8080);

            StringBuffer stringBuffer = new StringBuffer("GET " + uri + " HTTP/1.1\r\n");

            //意思意思的写了几个
            stringBuffer.append("Accept: */*\r\n");
            stringBuffer.append("Accept-Language: zh-cn\r\n");
            stringBuffer.append("Accept-Encoding: gzip, deflate\r\n");
            stringBuffer.append("Host: localhost:8080\r\n");
            stringBuffer.append("Connection: Keep-Alive\r\n\r\n");

            OutputStream outputStream = socket.getOutputStream();

            System.out.println(stringBuffer.toString());
            outputStream.write(stringBuffer.toString().getBytes());

            //等待服务器的响应结果
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            InputStream inputStream = socket.getInputStream();
            byte[] bytes = new byte[inputStream.available()];
            inputStream.read(bytes);
            System.out.println(new String(bytes));

        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                if (socket != null) {
                    socket.close();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

    }

}
