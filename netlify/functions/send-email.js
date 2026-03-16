// Netlify Function: send-email.js
// Sends form submissions and chat leads to loopstack2@gmail.com
// Requires GMAIL_APP_PASSWORD environment variable set in Netlify dashboard

const nodemailer = require('nodemailer');

exports.handler = async function (event) {
  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, body: 'Method Not Allowed' };
  }

  const gmailPass = process.env.GMAIL_APP_PASSWORD;
  if (!gmailPass) {
    return { statusCode: 500, body: JSON.stringify({ error: 'Email service not configured — GMAIL_APP_PASSWORD missing' }) };
  }

  let body;
  try {
    body = JSON.parse(event.body);
  } catch {
    return { statusCode: 400, body: JSON.stringify({ error: 'Invalid request body' }) };
  }

  const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
      user: 'loopstack2@gmail.com',
      pass: gmailPass
    }
  });

  const { type, first_name, last_name, email, company, service, message, name } = body;

  let subject, html;

  if (type === 'chat-lead') {
    subject = `💬 New Chat Lead — ${name || email}`;
    html = `
      <h2 style="color:#00E5FF;font-family:sans-serif">New Chat Lead</h2>
      <table style="font-family:sans-serif;font-size:15px;border-collapse:collapse">
        <tr><td style="padding:6px 16px 6px 0;color:#888">Name</td><td>${name || 'Not provided'}</td></tr>
        <tr><td style="padding:6px 16px 6px 0;color:#888">Email</td><td><a href="mailto:${email}">${email}</a></td></tr>
      </table>
      <p style="font-size:12px;color:#aaa;margin-top:24px">Sent from the LoopStack website chatbot</p>
    `;
  } else {
    subject = `📬 New Enquiry — ${first_name} ${last_name}`;
    html = `
      <h2 style="color:#00E5FF;font-family:sans-serif">New Contact Form Submission</h2>
      <table style="font-family:sans-serif;font-size:15px;border-collapse:collapse">
        <tr><td style="padding:6px 16px 6px 0;color:#888">Name</td><td>${first_name} ${last_name}</td></tr>
        <tr><td style="padding:6px 16px 6px 0;color:#888">Email</td><td><a href="mailto:${email}">${email}</a></td></tr>
        <tr><td style="padding:6px 16px 6px 0;color:#888">Company</td><td>${company || 'Not provided'}</td></tr>
        <tr><td style="padding:6px 16px 6px 0;color:#888">Service</td><td>${service || 'Not specified'}</td></tr>
        <tr><td style="padding:6px 16px 6px 0;color:#888;vertical-align:top">Message</td>
          <td style="max-width:480px">${(message || 'No message').replace(/\n/g, '<br>')}</td></tr>
      </table>
      <p style="font-size:12px;color:#aaa;margin-top:24px">Sent from the LoopStack website contact form</p>
    `;
  }

  try {
    await transporter.sendMail({
      from: '"LoopStack Website" <loopstack2@gmail.com>',
      to: 'loopstack2@gmail.com',
      replyTo: email,
      subject,
      html
    });

    return {
      statusCode: 200,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ success: true })
    };
  } catch (err) {
    return {
      statusCode: 500,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ error: 'Failed to send email', detail: err.message })
    };
  }
};
