function tablify(dictionary, headName) {
  if (typeof dictionary === "object") {
    html =`
    <table>
    <thead>
    <tr>
      <th colspan="2">` + headName + "</th>" +`
    </tr>
    </thead>
    <tbody>\n`;
    for (var key in dictionary) {
      html += "<tr>\n";
      html += "  <td>" + key + "</td>\n";
      html += "  <td " + ( (typeof dictionary[key] === "object") ? 'class=\'table-inside\'' : '') + " >" + tablify(dictionary[key], key) + "</td>\n";
      html += "</tr>\n\n";
    }
    html += `
    </tbody>
    </table>`;
  } else {
    html = dictionary;
  }
  return html
}
