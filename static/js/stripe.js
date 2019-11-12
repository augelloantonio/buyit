$(function () {
	$("#payment-form").submit(function () {
		$("#validate-card-btn").prop("disabled", true).html("Working...");
		var form = this;
		var card = {
			number: $("#id_credit_card_number").val(),
			expMonth: $("#id_expiry_month").val(),
			expYear: $("#id_expiry_year").val(),
			cvc: $("#id_cvv").val()
		};

		Stripe.createToken(card, function (status, response) {
			if (status === 200) {
				$("#credit-card-errors").hide();
				$("#id_stripe_id").val(response.id);
				$("#id_credit_card_number").removeAttr('name');
				$("#id_cvv").removeAttr('name');
				$("#id_cvv").removeAttr('name');
				$("#id_expiry_month").removeAttr('name');
				$("#id_expiry_year").removeAttr('name');

				form.submit();
			} else {
				$("#stripe-error-message").text(response.error.message);
				$("#credit-card-errors").show();
				$("#stripe-error-message").slideDown();
				setTimeout(() => {
					$("#stripe-error-message").slideUp(2000);
				}, 4000);
				$("#validate-card-btn").prop("disabled", false).html("Pay Fee");
			}
		});
		return false;
	});
});