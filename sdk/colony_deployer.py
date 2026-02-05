import json

class ColonyDeployer:
    @staticmethod
    def generate_deployment_manifest(chain_name):
        with open('sdk/colony_config.json', 'r') as f:
            config = json.load(f)
        
        target = config['empire_standard']['supported_chains'].get(chain_name)
        if not target:
            return "❌ Target chain not found in registry."
            
        manifest = {
            "mission": f"COLONIZE_{chain_name.upper()}",
            "contract": "ShieldArbitrator.sol",
            "initial_tax": config['empire_standard']['tax_rate'],
            "kernel": config['empire_standard']['kernel_version']
        }
        return manifest

if __name__ == "__main__":
    deployer = ColonyDeployer()
    print("🚀 [V8.0] Generating Deployment Manifest for MONAD...")
    print(deployer.generate_deployment_manifest("monad_testnet"))
