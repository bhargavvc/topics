<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# 📘 Azure Static Web App: Disconnect Azure DevOps Provider

## 🎯 **Overview**

This guide documents the process of disconnecting an Azure DevOps build provider from an Azure Static Web App. This is typically needed when migrating CI/CD pipelines, switching to GitHub Actions, or removing automatic deployment connections.

***

## 📋 **Prerequisites**

- Access to Azure Portal
- Appropriate permissions on the Static Web App resource
- Static Web App name: `serina-docs`
- Resource Group: `Serina-Docs-RG`

***

## 🔧 **Step-by-Step Process**

### **STEP 1: Navigate to Your Static Web App**

#### Path:

```
Azure Portal → Static Web Apps → serina-docs
```


#### Detailed Navigation:

1. Open [Azure Portal](https://portal.azure.com)
2. Use the search bar at the top to search for "Static Web Apps"
3. Click on your Static Web App: **serina-docs**
4. You'll land on the resource page

#### What You'll See:

- Resource group: `Serina-Docs-RG`
- Subscription: `Serina - Azure - CSP`
- Location: Global
- Current source connection visible

***

### **STEP 2: Access Deployment Token Settings**

#### Navigation:

1. From the left sidebar, click **"Overview"**
2. Wait for the page to fully load (you'll see the Essentials section)
3. In the top toolbar, locate the **"Manage deployment token"** button
4. Click on **"Manage deployment token"**

#### Key Indicators on Overview Page:

- **Source**: Shows `Serina-Code-Docs (DevOps)` ← Confirms Azure DevOps connection
- **Deployment history**: Shows Azure DevOps pipeline runs
- **View workflow**: Links to the Azure DevOps pipeline YAML

***

### **STEP 3: Disconnect the Provider**

#### Look for These Options:

Once the deployment token management page opens, search for one of these disconnect options:

- ✅ **"Disconnect Azure DevOps provider"**
- ✅ **"Remove build provider"**
- ✅ **"Disconnect CI/CD"**
- ✅ **"Delete workflow connection"**
- ✅ **"Manage source control"** (may contain disconnect option)


#### Expected Layout:

```
Build Provider: Azure DevOps (Connected)
[ Disconnect ] button
```


#### Action:

1. Click the **"Disconnect"** button
2. Confirm the action if prompted
3. Wait for the disconnection to complete

***

## 🖼️ **Visual Reference**

### Overview Page Structure:

```
┌─────────────────────────────────────────────────┐
│ serina-docs | Static Web App                    │
├─────────────────────────────────────────────────┤
│ [View app] [Refresh] [Delete] [Manage token] ← │
├─────────────────────────────────────────────────┤
│                                                 │
│ Essentials                                      │
│                                                 │
│ Resource group: Serina-Docs-RG                 │
│ Source: Serina-Code-Docs (DevOps) ← Key Info  │
│ Deployment history: Azure DevOps pipeline runs │
│                                                 │
└─────────────────────────────────────────────────┘
```


***

## ⚠️ **Important Notes**

### What Happens After Disconnection:

1. ✅ Static Web App continues to run with current deployment
2. ✅ Existing production site remains accessible
3. ❌ No automatic deployments from Azure DevOps
4. ❌ Pipeline no longer has deployment permissions
5. 🔄 Can reconnect to different source (GitHub, GitLab, etc.)

### Data Preservation:

- **Preserved**: Current deployment, custom domains, SSL certificates, environment variables
- **Removed**: Azure DevOps integration, automatic deployment trigger
- **Not Affected**: Application code, configurations, APIs

***

## 🔍 **Troubleshooting**

### If "Manage deployment token" is not visible:

1. Check your RBAC permissions (need Contributor or Owner role)
2. Refresh the page
3. Try accessing from the Configuration → Deployment settings

### If disconnection fails:

1. Ensure no active deployments are running
2. Check for any locks on the resource or resource group
3. Verify you have sufficient permissions
4. Try from Azure CLI:

```bash
az staticwebapp disconnect --name serina-docs --resource-group Serina-Docs-RG
```


### Alternative Navigation Path:

```
Static Web App → Configuration → General → Source control
```


***

## 🎓 **Use Cases**

### When to Disconnect Azure DevOps:

1. **Migration**: Moving to GitHub Actions or other CI/CD
2. **Manual Deployment**: Want to control deployments manually
3. **Pipeline Issues**: Troubleshooting deployment problems
4. **Security**: Rotating deployment tokens
5. **Architecture Change**: Switching to different deployment strategy

### When NOT to Disconnect:

- If you have active production deployments running
- If you don't have an alternative deployment method ready
- If the DevOps pipeline is working correctly and meeting needs

***

## 📝 **Related Azure CLI Commands**

```bash
# View current Static Web App details
az staticwebapp show --name serina-docs --resource-group Serina-Docs-RG

# Disconnect source control
az staticwebapp disconnect --name serina-docs --resource-group Serina-Docs-RG

# List deployment tokens
az staticwebapp secrets list --name serina-docs --resource-group Serina-Docs-RG

# Reset deployment token
az staticwebapp secrets reset-api-key --name serina-docs --resource-group Serina-Docs-RG
```


***

## 🔗 **Additional Resources**

- [Azure Static Web Apps Documentation](https://docs.microsoft.com/azure/static-web-apps/)
- [Deployment token management](https://docs.microsoft.com/azure/static-web-apps/deployment-token-management)
- [GitHub Actions deployment](https://docs.microsoft.com/azure/static-web-apps/github-actions-workflow)

***

## 📊 **Summary Checklist**

- [ ] Navigated to Static Web Apps in Azure Portal
- [ ] Located serina-docs Static Web App
- [ ] Accessed Overview page
- [ ] Clicked "Manage deployment token"
- [ ] Found disconnect/remove provider option
- [ ] Confirmed disconnection
- [ ] Verified source control is removed
- [ ] Planned alternative deployment strategy (if needed)

***

## 💡 **Key Takeaways**

1. **Non-destructive**: Disconnecting doesn't affect your running app
2. **Reversible**: You can reconnect to the same or different source
3. **Security**: Good practice when migrating or troubleshooting
4. **Permissions**: Requires appropriate Azure RBAC roles
5. **Planning**: Have alternative deployment method ready before disconnecting

***

**Document Created**: November 17, 2025
**Resource**: serina-docs Static Web App
**Action**: Azure DevOps Provider Disconnection
**Status**: Process documented for future reference

