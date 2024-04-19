provider "azurerm" {
  features {}
}


resource "azurerm_resource_group" "rg" {
  name     = "de-proj-rg"
  location = "UK South"
}

resource "azurerm_databricks_workspace" "databricks" {
  name                = "de-proj-workspace"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  sku                 = "standard"
}

resource "azurerm_mssql_server" "sqlserver" {
  name                         = "sensorsqlserver"
  resource_group_name          = azurerm_resource_group.rg.name
  location                     = azurerm_resource_group.rg.location
  version                      = "12.0"
  administrator_login          = "sqladmin0123"
  administrator_login_password = "#########"
}

resource "azurerm_sql_database" "sqldb" {
  name                = "sensorsqldb"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  server_name         = azurerm_mssql_server.sqlserver.name
  requested_service_objective_name = "S0"
}

resource "azurerm_storage_account" "storage" {
  name                     = "envsensorstorageacct"
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_storage_container" "container" {
  name                  = "sensorsdf-container"
  storage_account_name  = azurerm_storage_account.storage.name
  container_access_type = "private"
}


resource "azurerm_eventhub_namespace" "hubs" {
  name                = "sensorseventshub"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  sku                 = "Standard"
  capacity            = 1

  tags = {
    environment = "Production"
  }
}

resource "azurerm_eventhub" "hubs" {
  name                = "sensorseventhub"
  namespace_name      = azurerm_eventhub_namespace.hubs.name
  resource_group_name = azurerm_resource_group.rg.name
  partition_count     = 2
  message_retention   = 1
}

# Create containers for bronze, silver and gold layer
resource "azurerm_storage_container" "bronze" {
  name                  = "bronze"
  storage_account_name  = azurerm_storage_account.storage.name
  container_access_type = "private"
}

resource "azurerm_storage_container" "silver" {
  name                  = "silver"
  storage_account_name  = azurerm_storage_account.storage.name
  container_access_type = "private"
}

resource "azurerm_storage_container" "gold" {
  name                  = "gold"
  storage_account_name  = azurerm_storage_account.storage.name
  container_access_type = "private"
}

resource "azurerm_data_factory" "sensorsfactory" {
  name                = "sensorsfactory"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
}
