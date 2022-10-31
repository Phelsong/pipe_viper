# Pipe Viper Plugin

* This core plugin is meant simply for time savings and only uses the standard Python library, the goal is no additional dependencies.
* Plugins may take dependencies in the future  
  
__Currently only supports running a single `.ps1` or `string` Powershell command.__  
I plan to add support for command scripts and other shells, as well as supporting libraries of useful script functionality. Though, this plugin will be primarily focused on PowerShell related functionality unless someone else expands on other shell support.

* https://pypi.org/project/pipe-viper/

## Usage

```from pipe_viper.main import run_pwsh

ps1_path = "some/path/"
response = run_pwsh(ps1_path)```  

![alt text](./Screenshot 2022-10-31 133704.png)