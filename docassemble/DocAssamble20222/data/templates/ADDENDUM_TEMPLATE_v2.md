# **DO NOT FILE WITH COURT** {#do-not-file-with-court}

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><h1 id="plan-participant-information">Plan Participant
Information:</h1></td>
</tr>
<tr class="even">
<td>Name:</td>
<td>{{ participant.name }}</td>
</tr>
<tr class="odd">
<td>Address:</td>
<td>{{ participant.address.on_one_line() }}</td>
</tr>
<tr class="even">
<td>Date of Birth:</td>
<td>{{ format_date(participant.dob, format='MM/dd/yyyy') }}</td>
</tr>
<tr class="odd">
<td>Social Security Number:</td>
<td>({{ participant.ssn }})</td>
</tr>
<tr class="even">
<td>Phone:</td>
<td>({{ phone_number_part(participant.phone, 0) }})-{{
phone_number_part(participant.phone, 1) }}-{{
phone_number_part(participant.phone, 2) }}</td>
</tr>
<tr class="odd">
<td>E-Mail:</td>
<td>{{ participant.email }}</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><h1 id="alternate-payee-information">Alternate Payee
Information:</h1></td>
</tr>
<tr class="even">
<td>Name:</td>
<td>{% if who_is_participant == ‘Petitioner-Plaintiff’ %}{{
respondent.name }}{% else %}{{ petitioner.name }}{% endif %}</td>
</tr>
<tr class="odd">
<td>Address:</td>
<td>{{ alternate_payee.address.on_one_line() }}</td>
</tr>
<tr class="even">
<td>Date of Birth:</td>
<td>({{ format_date(alternate_payee.dob, format='MM/dd/yyyy') }})</td>
</tr>
<tr class="odd">
<td>Social Security Number:</td>
<td>({{ alternate_payee.ssn }})</td>
</tr>
<tr class="even">
<td>Phone:</td>
<td>({{ phone_number_part(alternate_payee.phone, 0) }})-{{
phone_number_part(alternate_payee.phone, 1) }}-{{
phone_number_part(alternate_payee.phone, 2) }}</td>
</tr>
<tr class="odd">
<td>E-Mail:</td>
<td>{{ alternate_payee.email }}</td>
</tr>
</tbody>
</table>
