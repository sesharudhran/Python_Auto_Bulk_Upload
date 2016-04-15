import java.util.ArrayList;
import java.util.Base64;
import java.util.HashMap;
import java.util.Map;
import java.util.UUID;
import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;

public class EncryptDecrypt {
	
	public static ArrayList<String> generateUUIDS(int count){
		Map<String, String> map = new HashMap<String, String>();
		
		ArrayList<String> where = new ArrayList<String>();
		
		for (int i=0; i<count; i++){
			
			UUID id = UUID.randomUUID();
			String strid = id.toString();
			where.add(strid);
//			System.out.println( strid);
			
			//password
			String pwd = strid.concat("-"+i);
//			System.out.println(pwd); 
			map.put(strid, pwd);
		}
//		System.out.println( where); 
			
		
//		System.out.println(map);
		return where;
	}
	
	public static Map<String,String> generateUUIDS1(int count){
		Map<String, String> map = new HashMap<String, String>();
		
		for (int i=0; i<count; i++){
			
			UUID id = UUID.randomUUID();
			String strid = id.toString();

			//password
			String pwd = strid.concat("-"+i);
 
			map.put(strid, pwd);
		}
//		System.out.println( where); 
			
		
//		System.out.println(map);
		return map;
	}
	
	
	public static String encrypt(String strToEncrypt)
    {
        String key = "sDkjhfkj8yhn8gig";

        try
        {
            Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5PADDING");
            byte[] keyData = key.getBytes("UTF-8");
            byte[] iv = new byte[cipher.getBlockSize()];
            IvParameterSpec ivSpec = new IvParameterSpec(iv);

            final SecretKeySpec secretKey = new SecretKeySpec(keyData, "AES");
            cipher.init(Cipher.ENCRYPT_MODE, secretKey,ivSpec);
            final String encryptedString = Base64.getEncoder().encodeToString(cipher.doFinal(strToEncrypt.getBytes()));
           
            return encryptedString;
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
        return null;
    }
	
        
	public static String decrypt(String strToDecrypt)
	   {
	        String key = "sDkjhfkj8yhn8gig";
	        try
	        {
	            Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5PADDING");
	            byte[] iv = new byte[cipher.getBlockSize()];
	            IvParameterSpec ivSpec = new IvParameterSpec(iv);
	            byte[] keyData = key.getBytes("UTF-8");

	            final SecretKeySpec secretKey = new SecretKeySpec(keyData, "AES");
	            cipher.init(Cipher.DECRYPT_MODE, secretKey,ivSpec);
	            final String decryptedString = new String(cipher.doFinal(Base64.getDecoder().decode(strToDecrypt)));
	            return decryptedString;
	        }
	        catch (Exception e)
	        {
	            e.printStackTrace();

	        }
	        return null;
	    }
	
	public static void generateUDID(int count){
		for (int i=0; i<count; i++){
			
			UUID id = UUID.randomUUID();
			System.out.println(id);
		}
	}
             
    public static void main(String[] args) {
		// TODO Auto-generated method stub

    	/* to generate UDID
    	generateUDID(20);
    	*/
    	
    	String passArray [] = {"1e96a658-4794-4b93-bdb0-8c47d66a7c3f-292","00ce02e3-ebfc-4039-9b89-cb19203ba2b0-293", "fcf11166-731c-4958-8d51-e466bbf0703c-294","3a66d55c-8579-445e-a8b4-5734c090b1ec-295",
    							"89b96531-7890-44eb-a9e2-b198a71113e2-296","b44dcfee-1bd7-442d-8965-0c5308828c09-297","a1264018-66f4-4593-bffb-f6d73896d7ea-298","610deabe-5fb5-486d-b3e5-bdbfab082ed8-299",
    							"7fb644a8-3fe5-4d69-a08f-58024cb6e43c-300"
        };

        for(int i=0;i < passArray.length;i++){
            String enc = encrypt(passArray[i]);
            String decrypt = decrypt(enc);
//            System.out.println( enc + ":" + decrypt); 
            System.out.println( enc);
        }
        
//    	System.out.println("------------ decryption ------------");
//  
//    	for(int i=0;i < passArray.length;i++){
//            String decrypt = decrypt(passArray[i]);
//            String enc = encrypt(decrypt);
//            System.out.println( decrypt + ":" + enc); 
//        }
    	
	}

}
