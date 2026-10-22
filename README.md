# clock-window-envelope

## Français

Calculer les fenêtres de rendez-vous robustes aux erreurs d’horloge.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m clock_window_envelope examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Unifie les fenêtres adjacentes, les érode par l’intervalle d’erreur d’horloge, puis intersecte les disponibilités de chaque partie. Donne un instant témoin garanti pour tous les décalages déclarés, au lieu d’un simple chevauchement nominal.

### Limites

Intervalles semi-ouverts et temps entiers ; décalages constants bornés, sans dérive ni estimation orbitale. Ce modèle ne synchronise pas une horloge.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Compute rendezvous windows robust to clock error.

Synthetic data; no network access or secret required.

```sh
python -m clock_window_envelope examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Union adjacent windows, erode by clock-error intervals, then intersect every party’s availability. Returns a witness valid for all declared offsets, rather than mere nominal overlap.

### Limits

Half-open intervals and integer times; bounded constant offsets, no drift or orbit estimation. This model does not synchronize a clock.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Calcular ventanas de encuentro robustas al error de reloj.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m clock_window_envelope examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Une ventanas adyacentes, las erosiona por intervalos de error de reloj e intersecta disponibilidades. Devuelve un instante válido para todos los desfases declarados, no solo solapamiento nominal.

### Límites

Intervalos semiabiertos y tiempos enteros; desfases constantes acotados, sin deriva ni estimación orbital. Este modelo no sincroniza relojes.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://github.com/plexil-group/plexil
- https://www.rfc-editor.org/rfc/rfc5905

## Exemple d’entrée / Input example / Ejemplo de entrada

```json
{
  "parties": [
    {
      "id": "satellite",
      "windows": [
        [
          0,
          12
        ],
        [
          12,
          25
        ]
      ],
      "offset": [
        -2,
        3
      ]
    },
    {
      "id": "ground",
      "windows": [
        [
          5,
          22
        ]
      ],
      "offset": [
        -1,
        1
      ]
    }
  ]
}
```

FR : champs numériques dans les unités de la section méthode ; clés JSON techniques conservées. EN: numeric fields use the method section units; technical JSON keys are preserved. ES: los campos numéricos usan las unidades del método; se conservan las claves JSON técnicas.
