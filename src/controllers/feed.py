from factory import db
from flask import Blueprint, jsonify, request, make_response
from model import User, Session, Feed

bp = Blueprint('feed', __name__)


@bp.route('/all', methods=['GET'])
def get_all_feed():
    req_session_id = request.cookies.get('session_id')
    authorized, user_id = __check_user_authtorized(req_session_id)
    if not authorized:
        return __jsonResponse("user authorized", 401)

    feed = db.session.execute(db.select(Feed)).scalars()
    sorted_feed = feed.sort(key=lambda x: x.id)
    resp_feed = []
    for f in sorted_feed:
        user = db.session.execute(db.select(User).filter_by(id=f.user_id)).scalar_one()
        ext_feed = {
            "title": f.title,
            "format": f.format,
            "text": f.text,
            "url_for_preview": f.url_for_preview,
            "tags": f.tags,
            "author": user.first_name + ' ' + user.last_name
        }
        resp_feed.append(ext_feed)
    return __jsonResponse({"feeds": resp_feed}, 201)


@bp.route('/<int:feed_id>', methods=['GET'])
def get_feed_by_id(feed_id):
    req_session_id = request.cookies.get('session_id')
    authorized, user_id = __check_user_authtorized(req_session_id)
    if not authorized:
        return __jsonResponse("user authorized", 401)

    try:
        f = db.session.execute(db.select(Feed)).scalar_one()
    except:
        return __jsonResponse("incorrect id", 400)

    user = db.session.execute(db.select(User).filter_by(id=f.user_id)).scalar_one()
    ext_feed = {
        "id": f.id,
        "title": f.title,
        "content": f.text,
        "author_id": f.user_id,
        "preview_url": f.url_for_preview,
        "tags": f.tags,
        "author": user.first_name + ' ' + user.last_name
    }
    return __jsonResponse(ext_feed, 400)


@bp.route('/', methods=['PUT'])
def update_feed(user_id):
    data = request.get_json()

    req_session_id = request.cookies.get('session_id')
    authorized, user_id = __check_user_authtorized(req_session_id)

    if not authorized:
        return __jsonResponse("user unauthorized", 401)

    feed = Feed()

    feed.title = data.get("title") or feed.title
    feed.format = data.get("format") or feed.format
    feed.text = data.get("text") or feed.text
    feed.url_for_preview = data.get("url_for_preview") or feed.url_for_preview
    feed.tags = data.get("tags") or feed.tags
    db.commit()
    return __jsonResponse("feed updated", 201)


@bp.route('/', methods=['POST'])
def create_feed():
    data = request.get_json()

    req_session_id = request.cookies.get('session_id')
    authorized, user_id = __check_user_authtorized(req_session_id)

    if not authorized:
        return __jsonResponse("user unauthorized", 401)

    required = ["title", "format", "text", "url_for_preview", "tags", "user_id"]
    for r in required:
        if not data.get(r):
            return __jsonResponse(f"field {data.get(r)} required", 400)

    feed = Feed()

    feed.title = data.get("title")
    feed.format = data.get("format")
    feed.text = data.get("text")
    feed.url_for_preview = data.get("url_for_preview")
    feed.tags = data.get("tags")
    feed.user_id = data.get("user_id")

    db.session.add(feed)
    db.session.commit()

    return __jsonResponse("feed created", 201)


# Другие маршруты для пользователя (например, обновление, удаление и т.д.)

def __check_user_authtorized(req_session_id):
    try:
        session = db.session.execute(db.select(Session).filter_by(session_id=req_session_id)).scalar_one()
    except:
        return False, None

    return True, session.user_id


def __jsonResponse(resp: dict or str, code: int):
    if isinstance(resp, str):
        resp = {"info": resp}

    return make_response(jsonify(resp), code)
