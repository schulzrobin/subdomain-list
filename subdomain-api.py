from flask import Flask, jsonify, request
import sublist3r

app = Flask(__name__)

# Funktion, um Subdomains mit Sublist3r zu finden
def find_subdomains(domain):
    subdomains = sublist3r.main(domain, 40, None, ports=None, silent=True, verbose=False, enable_bruteforce=False, engines=None)
    return subdomains

# API-Endpoint für Subdomain-Suche
@app.route('/api/subdomains', methods=['GET'])
def get_subdomains():
    domain = request.args.get('d')
    if not domain:
        return jsonify({"error": "Bitte eine Domain angeben."}), 400
    
    try:
        subdomains = find_subdomains(domain)
        return jsonify({"domain": domain, "subdomains": subdomains})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host'0.0.0.0', port='80', debug=True)