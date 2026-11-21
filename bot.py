import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes

TOKEN = os.environ.get("TOKEN")
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

def keep_alive():
    port = int(os.environ.get("PORT", 10000))
    class H(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Bot is alive")
        def log_message(self, *a):
            pass
    HTTPServer(("0.0.0.0", port), H).serve_forever()

threading.Thread(target=keep_alive, daemon=True).start()

# ═══════════════════════════════════════
#  👑 MISS ESPOIR - UNIVERSAL BOT 👑
# ═══════════════════════════════════════

def menu_principal():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🌐 HTTP INJECTOR", callback_data="http"),
         InlineKeyboardButton("📱 HTTP CUSTOM", callback_data="hc")],
        [InlineKeyboardButton("⚡ NETMOD", callback_data="netmod"),
         InlineKeyboardButton("🔥 SSCUSTOM", callback_data="ss")],
        [InlineKeyboardButton("🌑 DARK TUNNEL", callback_data="dark"),
         InlineKeyboardButton("🚀 NAPSTERNETV", callback_data="nap")],
        [InlineKeyboardButton("📁 MES FICHIERS", callback_data="fichiers"),
         InlineKeyboardButton("🎓 FORMATIONS", callback_data="formations")],
        [InlineKeyboardButton("👑 MISS ESPOIR VIP", callback_data="vip")],
    ])

def cadre(titre, lignes):
    texte = f"╔══════════════════════════╗\n"
    texte += f"║  {titre}  \n"
    texte += f"╠══════════════════════════╣\n"
    for l in lignes:
        texte += f"║  {l}\n"
    texte += f"╚══════════════════════════╝\n"
    return texte

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texte = (
        "╔══════════════════════════════════╗\n"
        "║                                  ║\n"
        "║   👑  BIENVENUE CHEZ  👑         ║\n"
        "║       ✨ MISS ESPOIR ✨         ║\n"
        "║                                  ║\n"
        "╠══════════════════════════════════╣\n"
        "║  Bonjour Maître, bienvenue dans  ║\n"
        "║  votre espace privé VIP.         ║\n"
        "║                                  ║\n"
        "║  Ici, nous créons VOS propres    ║\n"
        "║  fichiers VPN, avec VOTRE        ║\n"
        "║  serveur, de manière propre,     ║\n"
        "║  rapide et professionnelle.      ║\n"
        "║                                  ║\n"
        "║  Choisissez votre application    ║\n"
        "║  ci-dessous pour commencer. 👇   ║\n"
        "╚══════════════════════════════════╝\n\n"
        "🌸 *MISS ESPOIR vous souhaite une excellente connexion.* 🌸"
    )
    await update.message.reply_text(texte, reply_markup=menu_principal(), parse_mode="Markdown")

async def boutons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    data = q.data

    if data == "formations":
        await q.message.reply_text(
            "╔════════════════════════════╗\n"
            "║  🎓 FORMATIONS MISS ESPOIR  ║\n"
            "╠════════════════════════════╣\n"
            "║  1. Comment créer un serveur║\n"
            "║  2. Comment créer un fichier║\n"
            "║  3. Comment vendre vos fichiers║\n"
            "║  4. Formation VIP complète  ║\n"
            "╚════════════════════════════╝\n\n"
            "📩 Contactez MISS ESPOIR pour la formation complète."
        )
        return
    if data == "vip":
        await q.message.reply_text(
            "╔════════════════════════════╗\n"
            "║  👑 ESPACE VIP MISS ESPOIR  ║\n"
            "╠════════════════════════════╣\n"
            "║  Accès prioritaire          ║\n"
            "║  Fichiers illimités         ║\n"
            "║  Support 24h/24            ║\n"
            "╚════════════════════════════╝"
        )
        return
    if data == "fichiers":
        await q.message.reply_text("📁 Vos fichiers apparaîtront ici après création.")
        return

    context.user_data['app'] = data
    noms = {"http":"HTTP INJECTOR","hc":"HTTP CUSTOM","netmod":"NETMOD","ss":"SSCUSTOM","dark":"DARK TUNNEL","nap":"NAPSTERNETV"}
    nom = noms.get(data, data)
    await q.message.reply_text(
        f"╔════════════════════════════╗\n"
        f"║  ✅ {nom} SÉLECTIONNÉ  \n"
        f"╠════════════════════════════╣\n"
        f"║  Parfait Maître !            \n"
        f"║                            \n"
        f"║  Veuillez m'envoyer VOTRE    \n"
        f"║  serveur de cette manière :  \n"
        f"║                            \n"
        f"║  serveur.com:443:votre-uuid \n"
        f"║                            \n"
        f"║  Exemple :                 \n"
        f"║  monserveur.com:443:1234    \n"
        f"╚════════════════════════════╝"
    )

async def recevoir(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        serveur, port, uuid = update.message.text.strip().split(":")
        app = context.user_data.get('app', 'http')
        noms = {"http":"HTTP INJECTOR","hc":"HTTP CUSTOM","netmod":"NETMOD","ss":"SSCUSTOM","dark":"DARK TUNNEL","nap":"NAPSTERNETV"}
        nom_app = noms.get(app, app)

        texte_recu = (
            f"╔══════════════════════════════════╗\n"
            f"║   ✅ FICHIER CRÉÉ AVEC SUCCÈS    ║\n"
            f"╠══════════════════════════════════╣\n"
            f"║  👑 Par : MISS ESPOIR            ║\n"
            f"║  📱 Application : {nom_app}     \n"
            f"║  🌐 Serveur : {serveur}         \n"
            f"║  🔌 Port : {port}               \n"
            f"║  🆔 UUID : {uuid}               \n"
            f"╠══════════════════════════════════╣\n"
            f"║  Merci de votre confiance,       ║\n"
            f"║  Maître. Votre fichier est prêt. ║\n"
            f"║  Excellente connexion ! 🌸       ║\n"
            f"╚══════════════════════════════════╝"
        )
        contenu_fichier = (
            "╔══════════════════════════════════╗\n"
            "║      👑 MISS ESPOIR 👑            \n"
            "║   FICHIER OFFICIEL - ESPOIR      \n"
            "╠══════════════════════════════════╣\n"
            f"║ Application : {nom_app}\n"
            f"║ Serveur : {serveur}\n"
            f"║ Port : {port}\n"
            f"║ UUID : {uuid}\n"
            "╠══════════════════════════════════╣\n"
            "║ Merci d'utiliser MISS ESPOIR    \n"
            "║ Bonne connexion, Maître !        \n"
            "╚══════════════════════════════════╝\n"
        )
        await update.message.reply_text(texte_recu)
        await update.message.reply_document(document=contenu_fichier.encode(), filename=f"MISS-ESPOIR-{nom_app}.txt")
        await update.message.reply_text("👆 Voilà Maître, votre fichier est ci-dessus. Voulez-vous créer un autre fichier ? Tapez /start", reply_markup=menu_principal())
    except:
        await update.message.reply_text(
            "╔════════════════════════════╗\n"
            "║  ❌ ERREUR DE FORMAT        ║\n"
            "╠════════════════════════════╣\n"
            "║  Veuillez écrire comme ça : ║\n"
            "║  serveur.com:443:uuid       ║\n"
            "╚════════════════════════════╝"
        )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(boutons))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, recevoir))
app.run_polling()
