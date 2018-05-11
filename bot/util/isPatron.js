const fs = require("fs");

exports.run = (Client, Embed, guilds, role, id, msg, message) => {

    texts = JSON.parse(fs.readFileSync( "./bot/json/lang/" + guilds[msg.guild.id].language + ".json", 'utf8'));

    var to_return = false;

    var guild = Client.guilds.get("403882830225997825");
    var members = guild.members.clone();

    if(members.has(id)) {
        var member = members.get(id);
        var roles = member.roles;

        if(roles.find("name", role) || roles.find("name", "Friend")) {
            to_return = true;
        } else {
            if(message) Embed.createEmbed(msg.channel, texts.no_patron1 + guilds[msg.guild.id].prefix + texts.no_patron2, texts.error_title);
            to_return = false;
        }
    } else {
        if(message) Embed.createEmbed(msg.channel, texts.not_server, texts.error_title);
        to_return = false;
    }
    
    return to_return;
}