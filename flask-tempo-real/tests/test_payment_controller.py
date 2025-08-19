def test_create_payment_pix(client):
  response = client.post("/payments/pix", json={"value": 100.0})
  data = response.get_json()

  assert response.status_code == 200
  assert "payment" in data
  assert data["payment"]["value"] == 100.0

def test_confirm_payment_pix(client):
  # cria um pagamento primeiro
  create_resp = client.post("/payments/pix", json={"value": 150.0})
  payment_id = create_resp.get_json()["payment"]["id"]
  bank_payment_id = create_resp.get_json()["payment"]["bank_payment_id"]

  # confirma
  confirm_resp = client.post("/payments/pix/confirmation", json={
    "bank_payment_id": bank_payment_id,
    "value": 150.0
  })
  data = confirm_resp.get_json()

  assert confirm_resp.status_code == 200
  assert data["message"] == "The payment has been confirmed"
