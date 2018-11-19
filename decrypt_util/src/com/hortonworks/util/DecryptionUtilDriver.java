package com.hortonworks.util;

import org.apache.hadoop.security.alias.CredentialProvider;
import org.apache.hadoop.security.alias.CredentialProvider.CredentialEntry;
import org.apache.hadoop.security.alias.CredentialProviderFactory;
import org.apache.hadoop.conf.Configuration;
import java.io.IOException;
import java.util.List;

public class DecryptionUtilDriver {

 public static final String CREDENTIAL_PROVIDER_PATH="hadoop.security.credential.provider.path";

 public static void main(String args[]) throws IOException {

  String alias = args[0];
  String provider = args[1]; 
  char[] pass = null;
  try {

      Configuration conf = new Configuration();
      conf.set(CredentialProviderFactory.CREDENTIAL_PROVIDER_PATH,provider);
      pass = conf.getPassword(alias);
      System.out.println("pswd : " + String.valueOf(pass));
    } catch (Exception e) {
   	e.printStackTrace();
    }

 }

}
