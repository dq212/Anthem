#write-html.py


import os

f = open('EmailTest-1.html', 'w')
img = './imgs/header_all.jpg'


directory = "CO"
if not os.path.exists(directory):
    os.makedirs(directory)

message= """<!DOCTYPE html>
<html
  lang="en"
  xmlns="http://www.w3.org/1999/xhtml"
  xmlns:v="urn:schemas-microsoft-com:vml"
  xmlns:o="urn:schemas-microsoft-com:office:office">
  <head>
    <meta charset="utf-8" />
    <!-- utf-8 works for most cases --> 
    <meta name="viewport" content="width=device-width" />
    <!-- Forcing initial-scale shouldn't be necessary -->
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <!-- Use the latest (edge) version of IE rendering engine -->
    <meta name="x-apple-disable-message-reformatting" />
    <!-- Disable auto-scale in iOS 10 Mail entirely -->
    <title>------------ title ---------</title>
    <!-- <title>Get quotes and enroll members - faster and easier than ever</title>  -->
    <!-- The title tag shows in email notifications, like Android 4.4. -->

    <!-- Web Font / @font-face : BEGIN -->
    <!-- NOTE: If web fonts are not required, lines 10 - 27 can be safely removed. -->

    <!-- Desktop Outlook chokes on web font references and defaults to Times New Roman, so we force a safe fallback font. -->
    <!--[if mso]>
      <style>
        * {
          font-family: Arial, sans-serif !important;
        }
      </style>
    <![endif]-->

    <!-- All other clients get the webfont reference; some will render the font and others will silently fail to the fallbacks. More on that here: http://stylecampaign.com/blog/2015/02/webfont-support-in-email/ -->
    <!--[if !mso]><!-->
    <!-- <link href="https://fonts.googleapis.com/css?family=Montserrat:300,500" rel="stylesheet"> -->
    <!--<![endif]-->

    <!-- Web Font / @font-face : END -->

    <!-- CSS Reset -->
    <style>
      /* What it does: Remove spaces around the email design added by some email clients. */
      /* Beware: It can remove the padding / margin and add a background color to the compose a reply window. */
      html,
      body {
        margin: 0 auto !important;
        padding: 0 !important;
        height: 100% !important;
        width: 100% !important;
      }

      /* What it does: Stops email clients resizing small text. */
      * {
        -ms-text-size-adjust: 100%;
        -webkit-text-size-adjust: 100%;
      }

      /* What it does: Centers email on Android 4.4 */
      div[style*="margin: 16px 0"] {
        margin: 0 !important;
      }

      /* What it does: Stops Outlook from adding extra spacing to tables. */
      table,
      td {
        mso-table-lspace: 0pt !important;
        mso-table-rspace: 0pt !important;
      }

      /* What it does: Fixes webkit padding issue. Fix for Yahoo mail table alignment bug. Applies table-layout to the first 2 tables then removes for anything nested deeper. */
      table {
        border-spacing: 0 !important;
        border-collapse: collapse !important;
        table-layout: fixed !important;
        /* margin: 0 auto !important; */
      }
      table table table {
        table-layout: auto;
      }

      /* What it does: Uses a better rendering method when resizing images in IE. */
      img {
        -ms-interpolation-mode: bicubic;
      }

      /* What it does: A work-around for email clients meddling in triggered links. */
      *[x-apple-data-detectors],	/* iOS */
        .x-gmail-data-detectors, 	/* Gmail */
        .x-gmail-data-detectors *,
        .aBn {
        border-bottom: 0 !important;
        cursor: default !important;
        color: inherit !important;
        text-decoration: none !important;
        font-size: inherit !important;
        font-family: inherit !important;
        font-weight: inherit !important;
        line-height: inherit !important;
      }

      /* What it does: Prevents Gmail from displaying an download button on large, non-linked images. */
      .a6S {
        display: none !important;
        opacity: 0.01 !important;
      }
      /* If the above doesn't work, add a .g-img class to any image in question. */
      img.g-img + div {
        display: none !important;
      }

      /* What it does: Prevents underlining the button text in Windows 10 */
      .button-link {
        text-decoration: none !important;
      }

      /* What it does: Removes right gutter in Gmail iOS app: https://github.com/TedGoas/Cerberus/issues/89  */
      /* Create one of these media queries for each additional viewport size you'd like to fix */
      /* Thanks to Eric Lepetit @ericlepetitsf) for help troubleshooting */
      @media only screen and (min-device-width: 375px) and (max-device-width: 413px) {
        /* iPhone 6 and 6+ */
        .email-container {
          min-width: 375px !important;
        }
      }
    </style>

    <!-- Progressive Enhancements -->
    <style>
      a:link {
        color: #2f7fc2;
      }
      a:visited {
        color: #2f7fc2;
      }

      a:hover {
        color: #2f7fc2;
      }
      a:active {
        color: #2f7fc2;
      }
      /* What it does: Hover styles for buttons */
      .button-td,
      .button-a {
        transition: all 100ms ease-in;
      }
      .button-td:hover,
      .button-a:hover {
        background: #555555 !important;
        border-color: #555555 !important;
      }

      /* Media Queries */
      @media screen and (min-width: 600px) {
        .header-all {
          display: block;
        }
        .header-mobile {
          display: none;
          /* margin:0 0 !important; */
        }
      }

      @media screen and (max-width: 599px) {
        .header-all {
          display: none;
        }
        .header-mobile {
          display: block;
        }
      }

      @media screen and (max-width: 480px) {
        /* What it does: Forces elements to resize to the full width of their container. Useful for resizing images beyond their max-width. */
        .fluid {
          width: 100% !important;
          max-width: 100% !important;
          height: auto !important;
          margin-left: auto !important;
          margin-right: auto !important;
        }

        /* What it does: Forces table cells into full-width rows. */
        .stack-column,
        .stack-column-center {
          display: block !important;
          width: 100% !important;
          max-width: 100% !important;
          direction: ltr !important;
        }
        /* And center justify these ones. */
        .stack-column-center {
          text-align: center !important;
        }

        /* What it does: Generic utility class for centering. Useful for images, buttons, and nested tables. */
        .center-on-narrow {
          text-align: center !important;
          display: block !important;
          margin-left: auto !important;
          margin-right: auto !important;
          float: none !important;
        }
        table.center-on-narrow {
          display: inline-block !important;
        }

        /* What it does: Adjust typography on small screens to improve readability */
        .email-container p {
          font-size: 17px !important;
          line-height: 22px !important;
        }
      }
    </style>

    <!-- What it does: Makes background images in 72ppi Outlook render at correct size. -->
    <!--[if gte mso 9]>
      <xml>
        <o:OfficeDocumentSettings>
          <o:AllowPNG /> <o:PixelsPerInch>96</o:PixelsPerInch>
        </o:OfficeDocumentSettings>
      </xml>
    <![endif]-->
  </head>
  <body
    width="100%"
    bgcolor="#ffffff"
    style="margin: 0; mso-line-height-rule: exactly;">
    <!-- <center style="width: 100%; background: #ffffff; text-align: left;"> -->

    <!-- Visually Hidden Preheader Text : BEGIN -->
    <!-- <div style="display:none;font-size:1px;line-height:1px;max-height:0px;max-width:0px;opacity:0;overflow:hidden;mso-hide:all;font-family: sans-serif;">
			(Optional) This text will appear in the inbox preview, but not the email body. It can be used to supplement the email subject line or even summarize the email's contents. Extended text preheaders (~490 characters) seems like a better UX for anyone using a screenreader or voice-command apps like Siri to dictate the contents of an email. If this text is not included, email clients will automatically populate it using the text (including image alt text) at the start of the email's body.
        </div> -->
    <!-- Visually Hidden Preheader Text : END -->

    <!--
            Set the email width. Defined in two places:
            1. max-width for all clients except Desktop Windows Outlook, allowing the email to squish on narrow but never go wider than 600px.
            2. MSO tags for Desktop Windows Outlook enforce a 600px width.
            Note: The Fluid and Responsive templates have a different width (600px). The hybrid grid is more "fragile", and I've found that 600px is a good width. Change with caution.
        -->
    <div style="max-width: 600px; margin: auto;" class="email-container">
      <!--[if mso]>
            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="600" align="center">
            <tr>
            <td>
            <![endif]-->

      <!-- Email Body : BEGIN -->
      <table
        role="presentation"
        cellspacing="0"
        cellpadding="0"
        border="0"
        align="left"
        width="100%"
        style="max-width: 600px;"
        class="email-container">
        <!-- HEADER : BEGIN -->
        <tr>
          <td bgcolor="#ffffff">
            <table
              role="presentation"
              cellspacing="0"
              cellpadding="0"
              border="0"
              width="100%">
              <tr>
                <td style="padding: 30px 0px 10px 0px; text-align: left;">
                  <img
                    src="{img}"
                    width="600"
                    height="60"
                    alt="Time matters for you and your customers." 
                    border="0"
                    style="height: auto; font-family: sans-serif; font-size: 15px; line-height: 20px; color: #000000;"/>
                </td>
              </tr>
            </table>
          </td>
        </tr>
        <!-- HEADER : END -->

        <!-- HERO : BEGIN -->
        <tr>
          <!-- Bulletproof Background Images c/o https://backgrounds.cm -->
          <td
            bgcolor="#ffffff"
            align="left"
            valign="top"
            style="text-align: left; background-position: center center !important; background-size: cover !important;">
            <!--[if gte mso 9]>
                        <v:rect xmlns:v="urn:schemas-microsoft-com:vml" fill="true" stroke="false" style="width:600px; height:260px; background-position: center center !important;">
                        <v:fill type="tile" src="background.png" color="#000000" />
                        <v:textbox inset="0,0,0,0">
                        <![endif]-->
            <div>
              <!--[if mso]>
                            <table role="presentation" border="0" cellspacing="0" cellpadding="0" align="center" width="600">
                            <tr>
                            <td align="center" valign="middle" width="600">
                            <![endif]-->
              <table
                role="presentation"
                border="0"
                cellpadding="0"
                cellspacing="0"
                align="left"
                width="100%"
                style="max-width:600px; margin: auto;">
                <tr>
                  <td align="left" valign="middle">
                    <table>
                      <tr>
                        <td
                          class="header-all"
                          valign="top"
                          style="padding: 0px 0 0px 0px;">
                          <a href="#"
                            ><img
                              src="./imgs/header_all.jpg"
                              width="600"
                              height="265"
                              style="margin:0; padding:0; border:none; display:block;"
                              border="0"
                              alt=""/>
                          </a>
                        </td>
                      </tr>
                    </table>
                  </td>
                </tr>
              </table>

              <!--[if mso]>
                            </td>
                            </tr>
                            </table>
                            <![endif]-->
            </div>
            <!--[if gte mso 9]>
                        </v:textbox>
                        </v:rect>
                        <![endif]-->
          </td>
        </tr>
        <!-- HERO : END -->

        <!-- INTRO : BEGIN -->
        <tr>
          <td bgcolor="#ffffff">
            <table
              role="presentation"
              cellspacing="0"
              cellpadding="0"
              border="0"
              width="100%">
              <tr>
                <td
                  style="padding: 30px 40px 10px 40px; font-family: sans-serif; font-size: 15px; line-height: 20px; color: #000000; text-align: left; font-weight:normal;">
                  Dear [Personalized],
                </td>
              </tr>
              <tr>
                <td
                  style="padding: 10px 40px 0px 40px; font-family: sans-serif; font-size: 15px; line-height: 20px; color: #000000; text-align: left; font-weight:normal;">
                  <p style="margin: 0;">
                    We've spent a lot of time listening to brokers and customers and the end result is an enhanced plan portfolio. You'll see a new focus on simplicity and choice of cost savings.
                  </p>
                  <p>
                    And it's all done to help make your job more efficient - while delivering the health care solutions your customers and their employees want.
                  </p>
                  <p
                    style=" font-family: sans-serif; font-size: 15px; line-height: 20px; color: #000000; text-align: left; font-weight:bold;">
                    For 2019, we offer Colorado 14 plan designs on three networks. Including our new Platinum Plan that offers richer benefits across all three networks.</p>
                </td>
              </tr>

              <tr>
                <td
                  style="padding: 0px 40px 20px 40px; font-family: sans-serif; font-size: 15px; line-height: 20px; color: #000000; text-align: left; font-weight:normal;">
                  <span style="margin: 0;">
                    If you have questions, please call me at [XXX-XXX-XXXX] or email me. I'm here to help you.
                  </span>
                </td>
              </tr>
              <tr>
                <td
                  style="padding: 0px 40px 20px 40px; font-family: sans-serif; font-size: 15px; line-height: 20px; color: #000000; text-align: left; font-weight:normal;">
                  <p style="margin: 0;">Best,</p>
                </td>
              </tr>
              <tr>
                <td
                  style="padding: 0px 40px 20px 40px; font-family: sans-serif; font-size: 15px; line-height: 20px; color: #000000; text-align: left; font-weight:normal;">
                  <p style="margin: 0;">[Anthem Representative]<br />[Title]</p>
                </td>
              </tr>
            </table>
          </td>
        </tr>
      </table>

      <!-- INTRO : END -->

      <!-- Email Body : END -->

      <!--[if mso]>
            </td>
            </tr>
            </table>
            <![endif]-->
    </div>
  </body>
</html>
"""

f.write(message)
f.close()