%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<p>The opened items are as follows:</p>
<table border="1">
%for row in rows:
  <tr>
  %for col in row:
    <td>
      <a href="/item{{row[0]}}">
            {{col}}
      </a>
    </td>
  %end
    <td>
      <a href="/edit/{{row[0]}}">
            edit
      </a>
    </td>
  </tr>
%end
</table>

<div>
  <a href="/new">
    new item
  </a>
</div>
<div>
  <a href="/help">
    help
  </a>
</div>