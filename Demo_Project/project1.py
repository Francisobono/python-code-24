import requests
from urllib.parse import urlparse

def validate_url(url):
    """
    Vérifie si l'URL contient un schéma HTTP ou HTTPS.
    
    Args:
        url (str): L'URL à vérifier.
    
    Returns:
        bool: True si l'URL est valide, sinon False.
    """
    parsed = urlparse(url)
    return parsed.scheme in ("http", "https")

def check_endpoint(url):
    """
    Vérifie si un point de terminaison est accessible.
    
    Args:
        url (str): L'URL du point de terminaison.
    
    Returns:
        dict: Un dictionnaire contenant le statut et les détails de la réponse.
    
    Raises:
        ValueError: Si l'URL n'est pas valide ou manque le schéma HTTP/HTTPS.
        requests.RequestException: En cas d'échec de la requête.
    """
    # Vérification de l'URL
    if not validate_url(url):
        raise ValueError(f"L'URL '{url}' n'a pas un schéma HTTP ou HTTPS valide.")
    
    try:
        # Envoi de la requête GET
        response = requests.get(url, timeout=5)
        # Renvoi des détails de la réponse
        return {
            "url": url,
            "status_code": response.status_code,
            "is_successful": response.ok
        }
    except requests.RequestException as e:
        # Capture des erreurs liées à la requête
        raise requests.RequestException(f"Erreur lors de la vérification de l'URL '{url}': {e}")

def main():
    """
    Fonction principale pour vérifier plusieurs points de terminaison.
    """
    # Liste des URL à vérifier
    endpoints = [
        "http://example.com",
        "https://example.com",
        "ftp://example.com",  # Cette URL provoquera une exception
        "example.com"  # Cette URL manque le schéma et provoquera une exception
    ]
    
    for endpoint in endpoints:
        try:
            result = check_endpoint(endpoint)
            print(f"[SUCCESS] URL: {result['url']}, Status Code: {result['status_code']}")
        except ValueError as ve:
            print(f"[ERROR] Validation: {ve}")
        except requests.RequestException as re:
            print(f"[ERROR] Request: {re}")

if __name__ == "__main__":
    main()
