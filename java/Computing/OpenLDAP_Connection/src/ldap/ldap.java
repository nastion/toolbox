package ldap;

import javax.naming.*;
import javax.naming.directory.*;

import java.util.Hashtable;


public class ldap {
	public static void main(String[] args) {

		// Set up environment for creating initial context
		Hashtable env = new Hashtable(11);
		env.put(Context.INITIAL_CONTEXT_FACTORY, 
		    "com.sun.jndi.ldap.LdapCtxFactory");
		
		env.put(Context.PROVIDER_URL, "ldap://10.0.106.58:389/dc=ldapmaster,dc=syt-lab,dc=rocks");

		
		env.put(Context.SECURITY_AUTHENTICATION, "simple");
		env.put(Context.SECURITY_PRINCIPAL, "cn=admin,dc=ldapmaster,dc=syt-lab,dc=rocks");
		env.put(Context.SECURITY_CREDENTIALS, "root");

		try {
		    // Create initial context
		    DirContext ctx = new InitialDirContext(env);
		    
		    System.out.println(ctx.getNameInNamespace());
		    System.out.println(ctx.lookup("cn=owner"));
		    System.out.println(ctx.getEnvironment());

		    // do something useful with ctx
		    

		    // Close the context when we're done
		    ctx.close();
		} catch (NamingException e) {
		    e.printStackTrace();
		}
	}
}
