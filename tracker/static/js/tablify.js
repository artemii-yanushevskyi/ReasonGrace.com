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

function tablifylist(list, headName) {
  if (typeof list === "object") {
    html =`
    <table>
    <thead>
    <tr>
      <th colspan="2">` + headName + "</th>" +`
    </tr>
    </thead>
    <tbody>\n`;
    for (var i = 0; i < list.length; i++) {
      // Iterate over numeric indexes
      html += "<tr>\n";
      html += "  <td>" + list[i][0] + "</td>\n";
      html += "  <td " + ( (typeof list[i][1] === "object") ? 'class=\'table-inside\'' : '') + " >" + tablifylist(list[i][1], list[i][0]) + "</td>\n";
      html += "</tr>\n\n";
    }
    html += `
    </tbody>
    </table>`;
  }
  else {
    html = list;
  }

  return html
}
