///////// using rest assured

package com.rak.api_auto;
import io.restassured.path.json.JsonPath;
import io.restassured.response.Response;
import io.restassured.specification.RequestSpecification;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;
import static org.testng.Assert.assertEquals;
import static org.testng.AssertJUnit.assertTrue;
import io.restassured.RestAssured;
import io.restassured.matcher.RestAssuredMatchers.*;

import org.hamcrest.Matchers.*;

public class RestAssuredLearning {
    @Test(groups = "restAssured1")
    public void testGet() {
        System.out.println("Get call<<<<<");
        RestAssured.baseURI = "http://localhost:8082/user";
        RequestSpecification httpRequest = RestAssured.given();
        Response response = httpRequest.get("?phone=+919880002720");
        JsonPath jsonPathEvaluator = response.jsonPath();
        System.out.println(response.statusCode());
        System.out.println(response.getBody().asString());
        System.out.println(response.getBody().asString().getClass());
        System.out.println(jsonPathEvaluator.get("deviceToken").toString());
        System.out.println(jsonPathEvaluator.get("phoneNumber").toString());
        assertEquals(jsonPathEvaluator.get("phoneNumber").toString(), "+919880002720");
    }
    @Test(groups = "restAssured")
    public void testPost() {
        System.out.println("Is it working ?????<<<<<");
        String input_payload_string = "{ \"deviceToken\": \"my_device_token\", \"firebaseId\": \"string\", \"id\": \"string\", \"phoneNumber\": \"string\"}";
        RestAssured.baseURI = "http://localhost:8082/user";
        RequestSpecification httpRequest = RestAssured.given();
        httpRequest.header("Content-Type", "application/json");
        httpRequest.body(input_payload_string);
        Response response = httpRequest.post("/register");
        JsonPath jsonPathEvaluator = response.jsonPath();
        System.out.println(response.statusCode());
        System.out.println(response.getBody().asString());
        System.out.println(response.getBody().asString().getClass());
        System.out.println(jsonPathEvaluator.get("deviceToken").toString());
        System.out.println(jsonPathEvaluator.get("phoneNumber").toString());
        assertEquals(jsonPathEvaluator.get("deviceToken").toString(), "my_device_token");
    }
}





////////////// pure java based requests
// package com.rak.api_auto;
//
// import com.google.gson.Gson;
// import com.google.gson.JsonObject;
// import com.google.gson.JsonParser;
// import com.rak.api_auto.utils;
// import org.apache.http.HttpRequest;
// import org.apache.http.client.methods.HttpPost;
// import sun.net.www.http.HttpClient;
//
// import java.io.*;
// import java.net.*;
// import java.util.List;
//
// import org.apache.http.HttpResponse;
// //import org.apache.http.client.methods.HttpPost;
// //import org.apache.http.impl.client.CloseableHttpClient;
// //import org.apache.http.impl.client.HttpClients;
//
// public class FirstMain {
//     public static void main(String[] args) {
//         utils ut = new utils();
//         String getUrl ="http://localhost:8082/user?phone=%2B919880002720";
//         try {
//             List<List<String>> out =   ut.readCsv("/Users/pruthvikumar/Documents/workspace/new_practice_project/src/test/testData/parkingspot_service_v2_test_cases.csv");
// //             temp = out.get(1);
// //            System.out.println(out.get(1).getClass());
// //            System.out.println(out.get(1).get(1));
// //            System.out.println(out.get(1).get(4));
// //            System.out.println(out.get(1).get(4).getClass());
//             jsonUt(out.get(1).get(4));
// //            getCall(getUrl,"");
//             postCall("http://localhost:8082/user/register","{ \"deviceToken\": \"string\", \"firebaseId\": \"string\", \"id\": \"string\", \"phoneNumber\": \"string\"}");
//         } catch (FileNotFoundException e) {
//             e.printStackTrace();
//         }
//     }
// public static void jsonUt(String jsonString){
//     Gson g = new Gson();
// //    JsonObject jsonObject = new JsonParser().parse("{\"name\": \"John\"}").getAsJsonObject();
//     String jout = g.toJson(jsonString);
//     CreateStation s = g.fromJson(jsonString, CreateStation.class);
//     System.out.println(s.type);
// //    System.out.println(jout);
// //    JSONParser parser = new JSONParser();
// //    JSONObject json = (JSONObject) parser.parse(stringToParse);
//
// }
// public static void getCall(String inputUrl,String inputJson)  {
//
//     try {
//         URL url = new URL(inputUrl);
//         HttpURLConnection con = null;
//         con = (HttpURLConnection) url.openConnection();
//         con.setRequestMethod("GET");
//         con.setRequestProperty("Accept", "application/json");
//         int responseCode = con.getResponseCode();
//         System.out.println("GET Response Code :: " + responseCode);
//         if (responseCode == HttpURLConnection.HTTP_OK) { // success
//             BufferedReader in = new BufferedReader(new InputStreamReader(
//                     con.getInputStream()));
//             String inputLine;
//             StringBuffer response = new StringBuffer();
//
//             while ((inputLine = in.readLine()) != null) {
//                 response.append(inputLine);
//             }
//             in.close();
//
//             // print result
// //            System.out.println(response.toString());
// //            System.out.println(response.toString().getClass());
// //            System.out.println(response.getClass());
//         } else {
//             System.out.println("GET request not worked");
//         }
//
//     } catch (IOException e) {
//         e.printStackTrace();
//     }
//
// }
//     public static void postCall(String inputUrl,String inputJson)  {
//
//         try {
//             URL url = new URL(inputUrl);
//             String jsonInputString = inputJson;
// //            input_data = "{"deviceToken": "string","firebaseId": "string","id": "string","phoneNumber": "string"}";
//
//             HttpURLConnection con = null;
//             con = (HttpURLConnection) url.openConnection();
//             con.setRequestMethod("POST");
//             con.setRequestProperty("Accept-Language", "en-US,en;q=0.5");
//             con.setRequestProperty("Content-Type","application/json");
// //            con.setRequestProperty("Accept", "application/json");
// //            try(OutputStream os = con.getOutputStream()) {
// //                byte[] input = jsonInputString.getBytes("utf-8");
// //                os.write(input, 0, input.length);
// //                os.close();
// //            }
// //            HttpPost post = new HttpPost("http://192.168.0.44:80");
//             con.setDoOutput(true);
//             DataOutputStream wr = new DataOutputStream(con.getOutputStream());
//             wr.writeBytes(inputJson);
//             wr.flush();
//             wr.close();
//
//
//             int responseCode = con.getResponseCode();
//             System.out.println("POST Response Code :: " + responseCode);
//             if (responseCode == HttpURLConnection.HTTP_CREATED) { // success
//                 BufferedReader in = new BufferedReader(new InputStreamReader(
//                         con.getInputStream()));
//                 String inputLine;
//                 StringBuffer response = new StringBuffer();
//
//                 while ((inputLine = in.readLine()) != null) {
//                     response.append(inputLine);
//                 }
//                 in.close();
//
//                 // print result
//                 System.out.println(response.toString());
//                 System.out.println(response.toString().getClass());
//                 System.out.println(response.getClass());
//             } else {
//                 System.out.println("POST request not worked");
//             }
//
//         } catch (Exception e) {
//             System.out.println(e.toString());
//
//             e.printStackTrace();
//         }
//
//     }
//
//
// }
// class CreateStation{
//     public List<String> attachmentIds;
//     public String id;
//     public String type;
// }
