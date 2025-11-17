<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Azure AD Authentication Implementation - Complete Documentation

## 📚 Learning Reference: Implementing Azure AD Authentication for Azure Static Web Apps


***

## 🎯 **Project Overview**

**Objective**: Implement Azure Active Directory (Azure AD) authentication for docs.serinaplus.com hosted on Azure Static Web Apps

**Initial State**: Documentation site was publicly accessible without authentication
**Target State**: Users must authenticate with Azure AD (Data Semantics organization) to access the site

***

## 🏗️ **Architecture Components**

### 1. **Azure Static Web App**

- **Name**: serina-docs
- **Resource Group**: Serina-Docs-RG
- **URL**: https://docs.serinaplus.com
- **Hosting**: MkDocs documentation site
- **Deployment**: Azure DevOps CI/CD pipeline


### 2. **Azure AD Tenant**

- **Tenant Name**: Data Semantics Pvt Ltd
- **Tenant ID**: `86fb359e-1360-4ab3-b90d-2a68e8c007b9`
- **Primary Domain**: DSglobal.onmicrosoft.com


### 3. **Authentication Flow**

```
User → docs.serinaplus.com → Azure AD Login → Authenticated Access
```


***

## 📝 **Implementation Steps**

### **Phase 1: Azure AD App Registration**

#### Step 1.1: Create App Registration

**Portal Path**: Azure Portal → Azure Active Directory → App registrations → New registration

**Configuration**:

- **Name**: Serina Docs Authentication
- **Supported account types**: Accounts in this organizational directory only (Single tenant)
- **Redirect URI**:
    - Platform: Web
    - URI: `https://docs.serinaplus.com/.auth/login/aad/callback`

**Result**:

- **Application (Client) ID**: `5fd540de-2c7c-4233-82d3-b6802d0fc4e0`
- **Directory (Tenant) ID**: `86fb359e-1360-4ab3-b90d-2a68e8c007b9`


#### Step 1.2: Create Client Secret

**Portal Path**: App Registration → Certificates \& secrets → New client secret

**Configuration**:

- **Description**: Serina Docs Static Web App Auth
- **Expiration**: 730 days (24 months) - Expires 11/17/2027
- **Value**: `wD.8Q~Nq7aStVz24NyGJI8...` (stored securely)

⚠️ **Important**: Copy the secret value immediately - it's only shown once!

***

### **Phase 2: Static Web App Configuration**

#### Step 2.1: Add Environment Variables

**Portal Path**: Azure Portal → serina-docs → Settings → Environment variables

**Variables to Add**:

```bash
Name: AZURE_CLIENT_ID
Value: 5fd540de-2c7c-4233-82d3-b6802d0fc4e0

Name: AZURE_CLIENT_SECRET
Value: <client-secret-value-from-step-1.2>
```

**Environment**: Production

#### Step 2.2: Update staticwebapp.config.json

**File Location**: `/staticwebapp.config.json` in repository root

**Configuration Structure**:

```json
{
  "auth": {
    "identityProviders": {
      "azureActiveDirectory": {
        "registration": {
          "openIdIssuer": "https://login.microsoftonline.com/86fb359e-1360-4ab3-b90d-2a68e8c007b9/v2.0",
          "clientIdSettingName": "AZURE_CLIENT_ID",
          "clientSecretSettingName": "AZURE_CLIENT_SECRET"
        }
      }
    }
  },
  "routes": [
    {
      "route": "/*",
      "allowedRoles": ["authenticated"]
    }
  ],
  "responseOverrides": {
    "401": {
      "redirect": "/.auth/login/aad",
      "statusCode": 302
    }
  }
}
```

**Key Configuration Elements**:

- **openIdIssuer**: Points to your Azure AD tenant's OAuth endpoint
- **clientIdSettingName**: References environment variable for Client ID
- **clientSecretSettingName**: References environment variable for Client Secret
- **routes**: Specifies which routes require authentication (`/*` = all routes)
- **allowedRoles**: `["authenticated"]` = any authenticated user
- **responseOverrides**: Redirects unauthorized users (401) to Azure AD login

***

## 🔑 **Key Concepts**

### **1. Static Web Apps Authentication**

Azure Static Web Apps provides built-in authentication with identity providers:

- Azure Active Directory
- GitHub
- Twitter
- Google
- Facebook
- Custom OpenID Connect providers


### **2. Environment Variables**

- Stored securely in Azure
- Not exposed in code repository
- Referenced in config using `SettingName` pattern
- Applied at runtime during deployment


### **3. Authentication Endpoints**

```
Login:    /.auth/login/aad
Logout:   /.auth/logout
User Info: /.auth/me
```


### **4. Authorization Roles**

- `authenticated`: Any logged-in user
- `anonymous`: Non-authenticated users
- Custom roles: Defined in your app logic

***

## 🚀 **Deployment Pipeline**

### **Pipeline Configuration**

**File**: `azure-static-web-apps-brave-stone-09e14da00.yml`

**Trigger**: Commits to Serina-Code-Docs branch

**Key Steps**:

1. Checkout code
2. Install Python \& dependencies
3. Build MkDocs documentation
4. Deploy to Azure Static Web App using `AzureStaticWebApp@0` task

**Deployment Token**: Required for authentication to Static Web App

- Stored in Azure DevOps pipeline variables
- Must be valid and not expired

***

## ⚠️ **Common Issues \& Solutions**

### **Issue 1: Login Popup Not Appearing**

**Symptoms**: Site loads without authentication prompt

**Possible Causes**:

1. Configuration file not deployed
2. Environment variables not set
3. Configuration syntax errors

**Solutions**:

- Verify environment variables in Azure Portal
- Check `staticwebapp.config.json` syntax
- Ensure pipeline deployed successfully
- Clear browser cache and test in incognito mode


### **Issue 2: Pipeline Deployment Failure**

**Error**: "deployment_token provided was invalid"

**Solution**:

1. Azure Portal → Static Web App → Overview
2. Click "Manage deployment token"
3. Reset token
4. Update token in Azure DevOps pipeline variable `deploymentToken`
5. Re-run pipeline

### **Issue 3: 401 Redirect Loop**

**Symptoms**: Continuous redirects to login page

**Possible Causes**:

- Incorrect redirect URI in app registration
- Mismatched tenant ID
- Invalid client secret

**Solutions**:

- Verify redirect URI matches exactly: `https://docs.serinaplus.com/.auth/login/aad/callback`
- Check tenant ID in `openIdIssuer` URL
- Regenerate client secret if expired

***

## 🧪 **Testing Checklist**

### **Pre-Deployment Testing**

- [ ] App registration created successfully
- [ ] Client secret copied and stored
- [ ] Environment variables added to Static Web App
- [ ] Configuration file updated with correct variable names
- [ ] Syntax validated (JSON)


### **Post-Deployment Testing**

- [ ] Pipeline completes successfully
- [ ] Visit site in incognito mode
- [ ] Login prompt appears
- [ ] Can authenticate with organization account
- [ ] Authenticated users can access content
- [ ] Logout functionality works
- [ ] Check `/.auth/me` endpoint returns user info

***

## 📊 **Configuration Reference**

### **Complete staticwebapp.config.json Template**

```json
{
  "auth": {
    "identityProviders": {
      "azureActiveDirectory": {
        "registration": {
          "openIdIssuer": "https://login.microsoftonline.com/<TENANT_ID>/v2.0",
          "clientIdSettingName": "AZURE_CLIENT_ID",
          "clientSecretSettingName": "AZURE_CLIENT_SECRET"
        },
        "login": {
          "loginParameters": ["scope=openid profile email"]
        }
      }
    }
  },
  "routes": [
    {
      "route": "/*",
      "allowedRoles": ["authenticated"]
    },
    {
      "route": "/api/*",
      "allowedRoles": ["authenticated"]
    }
  ],
  "navigationFallback": {
    "rewrite": "/index.html",
    "exclude": ["/_framework/*", "/css/*", "/js/*"]
  },
  "responseOverrides": {
    "401": {
      "redirect": "/.auth/login/aad",
      "statusCode": 302
    }
  },
  "globalHeaders": {
    "X-Frame-Options": "DENY",
    "X-Content-Type-Options": "nosniff"
  }
}
```


### **Environment Variables Template**

```
AZURE_CLIENT_ID=<your-client-id>
AZURE_CLIENT_SECRET=<your-client-secret>
```


***

## 🔐 **Security Best Practices**

1. **Secret Management**
    - Never commit secrets to repository
    - Use environment variables for sensitive data
    - Rotate secrets before expiration
    - Set appropriate expiration periods
2. **Access Control**
    - Use least-privilege principle
    - Implement role-based access if needed
    - Regularly review app registration permissions
    - Monitor authentication logs
3. **Configuration Security**
    - Keep tenant IDs in config (not sensitive)
    - Reference secrets via variable names only
    - Use HTTPS for all endpoints
    - Enable security headers

***

## 📚 **Additional Resources**

### **Microsoft Documentation**

- [Azure Static Web Apps Authentication](https://docs.microsoft.com/azure/static-web-apps/authentication-authorization)
- [Configure Azure AD](https://docs.microsoft.com/azure/static-web-apps/authentication-azure-active-directory)
- [App registration quickstart](https://docs.microsoft.com/azure/active-directory/develop/quickstart-register-app)


### **Configuration Examples**

- [Static Web Apps Config Schema](https://docs.microsoft.com/azure/static-web-apps/configuration)
- [Authentication configuration samples](https://github.com/Azure/static-web-apps)

***

## 🎓 **Key Learnings**

### **Technical Insights**

1. Azure Static Web Apps provide built-in authentication without custom code
2. Environment variables enable secure secret management
3. Configuration file controls routing and authorization
4. Deployment tokens must be valid for CI/CD pipelines

### **Azure DevOps Integration**

1. Pipeline automatically deploys on code commits
2. Deployment tokens authenticate pipeline to Static Web App
3. Failed deployments don't affect running production site
4. Manual pipeline re-runs available for fixes

### **Azure AD Concepts**

1. App registrations represent applications in Azure AD
2. Client ID identifies the application
3. Client Secret proves application identity
4. Redirect URI must match exactly for security
5. Tenant ID scopes authentication to organization

***

## ✅ **Final Implementation Status**

### **Completed**

- ✅ Azure AD app registration created
- ✅ Client ID and secret generated
- ✅ Environment variables configured in Static Web App
- ✅ Configuration file updated with proper settings
- ✅ Changes committed to repository


### **Pending**

- ⏳ Pipeline deployment token needs refresh
- ⏳ Re-run pipeline to deploy updated configuration
- ⏳ Final testing of authentication flow


### **Next Steps**

1. Reset deployment token in Azure Portal
2. Update token in Azure DevOps pipeline variables
3. Re-run pipeline: Build \#20251117.3
4. Test authentication at https://docs.serinaplus.com
5. Verify login popup appears for unauthenticated users

***

## 📝 **Quick Reference Commands**

### **Azure CLI**

```bash
# Get Static Web App details
az staticwebapp show --name serina-docs --resource-group Serina-Docs-RG

# List environment variables
az staticwebapp appsettings list --name serina-docs --resource-group Serina-Docs-RG

# Reset deployment token
az staticwebapp secrets reset-api-key --name serina-docs --resource-group Serina-Docs-RG
```


### **Testing Authentication**

```bash
# Check if authentication is working
curl -I https://docs.serinaplus.com/

# Should return 302 redirect to /.auth/login/aad
```


***

## 📅 **Project Timeline**

**Date**: November 17, 2025, 8-10 PM IST

**Duration**: ~2 hours

**Tasks Completed**:

1. Initial site assessment (no authentication)
2. Azure AD app registration (15 min)
3. Client secret generation (5 min)
4. Environment variable configuration (10 min)
5. Configuration file update (15 min)
6. Code commit and pipeline trigger (10 min)
7. Troubleshooting pipeline failure (30 min)
8. Documentation (30 min)

***

This documentation provides a complete reference for implementing Azure AD authentication on Azure Static Web Apps. Keep this for future projects or when troubleshooting authentication issues!

