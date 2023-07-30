using UnityEngine;

public class PlayerController : MonoBehaviour
{
    public float speed = 5f; // Geschwindigkeit des Spielers

    private Rigidbody2D rb;

    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
    }

    void Update()
    {
        // Eingabe erfassen
        float moveHorizontal = Input.GetAxis("Horizontal");
        float moveVertical = Input.GetAxis("Vertical");

        // Bewegungsrichtung basierend auf der Tasteneingabe festlegen
        Vector2 movement = new Vector2(moveHorizontal, moveVertical) * speed;

        // Bewegung an den Rigidbody übergeben
        rb.velocity = movement;
    }
}
